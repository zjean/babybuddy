# -*- coding: utf-8 -*-
from django.utils import timezone
from django.utils.translation import gettext as _

import plotly.offline as plotly
import plotly.graph_objs as go

from reports import utils


def breastpump_amounts(objects):
    """
    Create a graph showing breastpump amounts over time.
    :param instances: a QuerySet of Breastpump instances.
    :returns: a tuple of the the graph's html and javascript.
    """
    objects = objects.order_by("-time")

    trace = go.Scatter(
        name=_("Breastpump"),
        x=list(objects.values_list("time", flat=True)),
        y=list(objects.values_list("amount", flat=True)),
        fill="tozeroy",
    )

    layout_args = utils.default_graph_layout_options()
    layout_args["barmode"] = "stack"
    layout_args["title"] = _("<b>Breastpump</b>")
    layout_args["xaxis"]["title"] = _("Date")
    layout_args["xaxis"]["rangeselector"] = utils.rangeselector_date()
    layout_args["yaxis"]["title"] = _("Breastpump")

    fig = go.Figure({"data": [trace], "layout": go.Layout(**layout_args)})
    output = plotly.plot(fig, output_type="div", include_plotlyjs=False)
    return utils.split_graph_output(output)
