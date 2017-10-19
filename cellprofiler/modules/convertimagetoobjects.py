# coding=utf-8

"""
ConvertImageToObjects
=====================

**ConvertImageToObjects** converts a binary image to objects. Connected components of the binary image are assigned to
the same object. This module is useful for identifying objects that can be cleanly distinguished using **Threshold**.
If you wish to distinguish clumped objects, see **Watershed** or the **Identify** modules.

Note that grayscale images provided as input to this module will be converted to binary images. Pixel intensities
below or equal to 50% of the input's full intensity range are assigned to the background (i.e., assigned the value 0).
Pixel intensities above 50% of the input's full intensity range are assigned to the foreground (i.e., assigned the
value 1).

|

============ ============ ===============
Supports 2D? Supports 3D? Respects masks?
============ ============ ===============
YES          YES          NO
============ ============ ===============

"""

import skimage
import skimage.measure

import cellprofiler.module
import cellprofiler.setting


class ConvertImageToObjects(cellprofiler.module.ImageSegmentation):
    category = "Advanced"

    module_name = "ConvertImageToObjects"

    variable_revision_number = 1

    def create_settings(self):
        super(ConvertImageToObjects, self).create_settings()

        self.background_label = cellprofiler.setting.Integer(
            "Background label",
            value=0
        )

        self.connectivity = cellprofiler.setting.Integer(
            "Connectivity",
            minval=1,
            value=1
        )

    def settings(self):
        settings = super(ConvertImageToObjects, self).settings()

        settings += [
            self.background_label,
            self.connectivity
        ]

        return settings

    def visible_settings(self):
        visible_settings = super(ConvertImageToObjects, self).visible_settings()

        visible_settings += [
            self.background_label,
            self.connectivity
        ]

        return visible_settings

    def run(self, workspace):
        self.function = lambda x_data, background_label, connectivity: skimage.measure.label(
            skimage.img_as_bool(x_data),
            background=background_label,
            connectivity=connectivity
        )

        super(ConvertImageToObjects, self).run(workspace)
