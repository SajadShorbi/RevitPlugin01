# -*- coding: utf-8 -*-

# IMPORTS
import Autodesk.Revit.DB

# VARAIBLES
uidoc= __revit__.ActiveUIDocument
doc=  __revit__.ActiveUIDocument.Document

# FUNCTIONS
def get_selected_elements(uidoc):
    """This Function will return elements have selected in Revit UI
    :param uidoc: uidoc where elements are selected.
    :return:      list of selected elements"""
    selected_elements = []
    for elem_id in uidoc.Selection.GetElementIds():
        elem = uidoc.Document.GetElement(elem_id)
        selected_elements.append(elem)
    return selected_elements