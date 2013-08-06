# Powerline eXtenstion for ci-status

This is a fork of (plenv segment plugin)[https://github.com/omega/powerlinex-segment-plenv] by (omega)[http://github.com/omega].

Changed to work with ci-status and display Continious Integration status.

First install the addon:

    pip install -U --user git+https://github.com/tilljoel/powerlinex-segment-ci-status.git

If you make a theme, you can include a custom `segment_data`:

    "version": {
        "before": "ⓔ  "
    },

And then add this to your prefered spot under `segments`:

    {
        "module": "powerlinex.segment.ci-status",
        "name": "version"
    },


The `highlight_group` of the segment returned is `ruby_version`, `virtualenv`,
in that order. This will be highlighted in the same way as `virtualenv`, unless
you specify something else in the `ruby_version` color.
