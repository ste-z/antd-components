import dash
import json
import uuid
import numpy as np
from flask import request
from dash import html
from requests import options
import feffery_antd_components as fac
from dash.dependencies import Input, Output, ALL
from faker import Faker

faker = Faker(locale='zh_CN')

app = dash.Dash(
    __name__
)

app.layout = html.Div(
    [

        fac.AntdSpace(
            [
                fac.AntdButton(
                    '触发2秒自定义骨骼屏动画', id='skeleton-custom-demo-input',
                    type='primary'
                ),

                fac.AntdCustomSkeleton(
                    fac.AntdTable(
                        columns=[
                            {
                                'title': '国家名示例',
                                'dataIndex': '国家名示例',
                                'width': '25%'
                            },
                            {
                                'title': '省份名示例',
                                'dataIndex': '省份名示例',
                                'width': '25%'
                            },
                            {
                                'title': '城市名示例',
                                'dataIndex': '城市名示例',
                                'width': '25%'
                            },
                            {
                                'title': '日期示例',
                                'dataIndex': '日期示例',
                                'width': '25%'
                            }
                        ],
                        bordered=True,
                        data=[
                            {
                                'key': i,
                                '国家名示例': faker.country(),
                                '省份名示例': faker.province(),
                                '城市名示例': faker.city_name(),
                                '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None)
                            }
                            for i in range(3)
                        ]
                    ),
                    id='custom-skeleton-demo',
                    skeletonContent=html.Div(
                        [
                            fac.AntdRow(
                                [
                                    fac.AntdCol(
                                        fac.AntdSkeletonButton(
                                            block=True,
                                            active=True
                                        ),
                                        span=6,
                                        style={
                                            'padding': '4px'
                                        }
                                    )
                                ] * 16
                            ),
                            fac.AntdSpace(
                                [
                                    html.Div(
                                        fac.AntdSkeletonButton(
                                            active=True,
                                            size='small',
                                            block=True
                                        ),
                                        style={
                                            'width': '80px'
                                        }
                                    ),
                                    html.Div(
                                        fac.AntdSkeletonButton(
                                            active=True,
                                            size='small',
                                            block=True
                                        ),
                                        style={
                                            'width': '60px'
                                        }
                                    )
                                ],
                                style={
                                    'float': 'right',
                                    'paddingRight': '4px',
                                    'paddingTop': '15px'
                                }
                            )
                        ]
                    )
                ),
            ],
            direction='vertical',
            style={
                'width': '100%',
                'paddingBottom': '50px'
            }
        ),

        fac.AntdPopconfirm(
            fac.AntdButton(
                '点击触发',
                type='primary'
            ),
            title=html.Span(
                [
                    fac.AntdText('气泡确认', strong=True),
                    fac.AntdText('测试')
                ]
            )
        ),

        fac.AntdEmpty(
            fac.AntdButton('children测试', type='primary'),
            description=fac.AntdButton('description测试', type='primary'),
        ),

        fac.AntdAlert(
            type="success",
            showIcon=True,
            message="This is a success alert",
            description="This is a description",
            closable=True,
            action=fac.AntdSpace(
                [
                    fac.AntdButton('接受', type="primary"),
                    fac.AntdButton('拒绝', type="primary", danger=True),
                ],
                direction="vertical",
            )
        ),

        fac.AntdTabs(
            [
                fac.AntdTabPane(
                    html.Div(
                        '标签页1测试',
                        style={
                            'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                            'height': '200px',
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    ),
                    tab='标签页1',
                    key='标签页1'
                ),
                fac.AntdTabPane(
                    html.Div(
                        fac.AntdButton('标签页2测试', type='primary'),
                        style={
                            'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                            'height': '200px',
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    ),
                    tab='标签页2',
                    key='标签页2'
                ),
                fac.AntdTabPane(
                    html.Div(
                        fac.AntdButton('标签页3测试', type='dashed'),
                        style={
                            'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                            'height': '200px',
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    ),
                    tab='标签页3',
                    key='标签页3'
                )
            ],
            tabBarGutter=50,
            tabPaneAnimated=True,
            tabBarLeftExtraContent=html.Div(
                fac.AntdButton('测试', type='primary'),
                style={
                    'padding': '0 20px',
                    'display': 'flex',
                    'justifyContent': 'center'
                }
            ),
            tabBarRightExtraContent=html.Div(
                fac.AntdButton('测试', type='primary'),
                style={
                    'padding': '0 20px',
                    'display': 'flex',
                    'justifyContent': 'center'
                }
            )
        ),

        fac.AntdDatePicker(allowClear=False),

        fac.AntdDateRangePicker(allowClear=False)
    ],
    style={
        'padding': '100px'
    }
)


@app.callback(
    Output('custom-skeleton-demo', 'children'),
    Input('skeleton-custom-demo-input', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_custom_callback_demo(nClicks):
    import time
    time.sleep(2)

    return fac.AntdTable(
        columns=[
            {
                'title': '国家名示例',
                'dataIndex': '国家名示例',
                'width': '25%'
            },
            {
                'title': '省份名示例',
                'dataIndex': '省份名示例',
                'width': '25%'
            },
            {
                'title': '城市名示例',
                'dataIndex': '城市名示例',
                'width': '25%'
            },
            {
                'title': '日期示例',
                'dataIndex': '日期示例',
                'width': '25%'
            }
        ],
        bordered=True,
        data=[
            {
                'key': i,
                '国家名示例': faker.country(),
                '省份名示例': faker.province(),
                '城市名示例': faker.city_name(),
                '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None)
            }
            for i in range(3)
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=True)
