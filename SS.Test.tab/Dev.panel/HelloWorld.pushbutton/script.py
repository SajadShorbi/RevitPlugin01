__title__   ="Hello NLBO"
__Author__  ="Sajad Shorbi"
__doc__     ="""this is a hello NLBO button. click on it to see what happens..."""

# COSTEM IMPORTS

uidoc=__revit__.ActiveUIDocument
from Snippets._selection import get_selected_elements
if __name__ == '__main__':
    print(get_selected_elements(uidoc))


