
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
    # Check if the class is already an extension
    is_extension = False
    for ext in extensions:
        if class_name + '.' + ext == class_name:
            is_extension = True
            break
    if not is_extension:
        # If the class is not an extension, find the strongest extension
        strength = -1
        for ext in extensions:
            strength = min(strength, (len(''+class_name[0].upper()+ext) - len(ext)))
        return class_name + '.' + str(strength)
    else:
        # If the class is an extension, return the class
        return class_name
