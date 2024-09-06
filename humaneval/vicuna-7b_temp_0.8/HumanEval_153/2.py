
def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    # Check that the class_name is a valid class name
    if class_name not in __import__(".").__dict__['__all__']:
        raise ValueError("Class not found: {}".format(class_name))

    # Check that the class has an attribute 'extensions'
    if 'extensions' not in dir(class_name):
        raise ValueError("Class '{}' has no attribute 'extensions'".format(class_name))

    # Sort the list of extensions by strength
    extensions.sort(key=lambda x: -x[1], reverse=True)

    # Find the strongest extension and return the desired string
    return class_name + "." + extensions[0][0]
