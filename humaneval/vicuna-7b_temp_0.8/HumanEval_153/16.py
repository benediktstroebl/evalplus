
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
    # Get the number of uppercase and lowercase letters in the class name
    class_name_length = len(class_name.upper())
    class_name_lower = class_name.lower()
    class_name_length_lower = len(class_name_lower)

    # Get the number of uppercase and lowercase letters in each extension name
    for ext in extensions:
        ext_name_length = len(ext.upper())
        ext_name_lower = ext.lower()
        ext_name_length_lower = len(ext_name_lower)

    # Find the strength of each extension
    strength = 0
    for i in range(len(extensions)):
        strength += class_name_length - ext_name_length_lower
        strength += class_name_length_lower - ext_name_length

    # Choose the extension with the highest strength
    return class_name + '.' + extensions[strength.max()]
