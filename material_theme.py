import plotly.graph_objs as go

# Use with
# import plotly.io as pio
# pio.templates["material_theme"] = material_theme

# pio.templates.default = "material_theme"
# or
# go.Figure(layout={"template": "material_theme"})

material_theme = go.layout.Template(
    {
        "data": {
            "bar": [
                {"marker": {"line": {"color": "white", "width": 0.5}}, "type": "bar"}
            ],
            "barpolar": [
                {
                    "marker": {"line": {"color": "white", "width": 0.5}},
                    "type": "barpolar",
                }
            ],
            "carpet": [
                {
                    "aaxis": {
                        "endlinecolor": "#414549",
                        "gridcolor": "#C8D4E3",
                        "linecolor": "#C8D4E3",
                        "minorgridcolor": "#C8D4E3",
                        "startlinecolor": "#414549",
                    },
                    "baxis": {
                        "endlinecolor": "#414549",
                        "gridcolor": "#C8D4E3",
                        "linecolor": "#C8D4E3",
                        "minorgridcolor": "#C8D4E3",
                        "startlinecolor": "#414549",
                    },
                    "type": "carpet",
                }
            ],
            "choropleth": [
                {"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}
            ],
            "contour": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#e1bee7"],
                        [0.25, "#ba68c8"],
                        [0.50, "#9c27b0"],
                        [0.75, "#7b1fa2"],
                        [1.0, "#4a148c"],
                    ],
                    "type": "contour",
                }
            ],
            "contourcarpet": [
                {"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}
            ],
            "heatmap": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#e1bee7"],
                        [0.25, "#ba68c8"],
                        [0.50, "#9c27b0"],
                        [0.75, "#7b1fa2"],
                        [1.0, "#4a148c"],
                    ],
                    "type": "heatmap",
                }
            ],
            "heatmapgl": [
                {"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "heatmapgl"}
            ],
            "histogram": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "histogram",
                }
            ],
            "histogram2d": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#e1bee7"],
                        [0.25, "#ba68c8"],
                        [0.50, "#9c27b0"],
                        [0.75, "#7b1fa2"],
                        [1.0, "#4a148c"],
                    ],
                    "type": "histogram2d",
                }
            ],
            "histogram2dcontour": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#e1bee7"],
                        [0.25, "#ba68c8"],
                        [0.50, "#9c27b0"],
                        [0.75, "#7b1fa2"],
                        [1.0, "#4a148c"],
                    ],
                    "type": "histogram2dcontour",
                }
            ],
            "mesh3d": [
                {"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}
            ],
            "parcoords": [
                {
                    "line": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "parcoords",
                }
            ],
            "scatter": [
                {
                    "marker": {
                        "colorbar": {"outlinewidth": 0, "ticks": ""},
                        "opacity": 0.5,
                        "size": 15,
                    },
                    "type": "scatter",
                }
            ],
            "scatter3d": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scatter3d",
                }
            ],
            "scattercarpet": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scattercarpet",
                }
            ],
            "scattergeo": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scattergeo",
                }
            ],
            "scattergl": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scattergl",
                }
            ],
            "scattermapbox": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scattermapbox",
                }
            ],
            "scatterpolar": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scatterpolar",
                }
            ],
            "scatterpolargl": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scatterpolargl",
                }
            ],
            "scatterternary": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scatterternary",
                }
            ],
            "surface": [
                {"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "surface"}
            ],
            "table": [
                {
                    "cells": {"fill": {"color": "#dadce0"}, "line": {"color": "white"}},
                    "header": {
                        "fill": {"color": "#C8D4E3"},
                        "line": {"color": "white"},
                    },
                    "type": "table",
                }
            ],
        },
        "layout": {
            "clickmode": "event+select",
            "colorscale": {
                "diverging": [
                    [0.0, "#e1bee7"],
                    [0.25, "#ba68c8"],
                    [0.50, "#9c27b0"],
                    [0.75, "#7b1fa2"],
                    [1.0, "#4a148c"],
                ],
                "sequential": [
                    [0.0, "#e1bee7"],
                    [0.25, "#ba68c8"],
                    [0.50, "#9c27b0"],
                    [0.75, "#7b1fa2"],
                    [1.0, "#4a148c"],
                ],
                "sequentialminus": [
                    [0.0, "#e1bee7"],
                    [0.25, "#ba68c8"],
                    [0.50, "#9c27b0"],
                    [0.75, "#7b1fa2"],
                    [1.0, "#4a148c"],
                ],
            },
            "colorway": [
                "#6200ee",
                "#00a2ac",
                "#ff8335",
                "#ff4193",
                "#007dee",
                "#c0ca33",
                "#ffc107",
                "#b00020",
            ],
            "font": {
                "color": "#7c7d80",
                "family": "Roboto, Open Sans, Segoe UI, Helvetica, sans-serif",
                "size": 12,
            },
            "hoverlabel": {
                "bgcolor": "#ffffff",
                "bordercolor": "#ffffff",
                "font": {
                    "color": "#414549",
                    "family": "Roboto, Open Sans, Segoe UI, Helvetica, sans-serif",
                    "size": 22,
                },
            },
            "legend": {"orientation": "h"},
            "shapedefaults": {"fillcolor": "#6200ee"},
            "title": {"font": {"color": "#414549", "size": 22}, "x": 0.05},
            "xaxis": {
                "automargin": True,
                "gridcolor": "#ebebeb",
                "linecolor": "#dadce0",
                "linewidth": 2.8,
                "showgrid": False,
                "tickcolor": "#dadce0",
                "tickwidth": 2.8,
                "zerolinecolor": "#dadce0",
                "zerolinewidth": 2.0,
                "showline": True,
                "ticks": "outside",
                "nticks": 8,
                "zeroline": False,
            },
            "yaxis": {
                "automargin": True,
                "gridcolor": "#ebebeb",
                "gridwidth": 1.5,
                "side": "right",
                "zerolinecolor": "#dadce0",
                "zerolinewidth": 2.0,
                "linecolor": "#dadce0",
                "tickcolor": "#dadce0",
                "tickwidth": 2.8,
                "linewidth": 2.8,
                "nticks": 8,
                "showline": False,
                "zeroline": True,
            },
        },
    }
)
