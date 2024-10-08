
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
    # check if the class name is in the list
    if class_name in extensions:
        # find the strongest extension
        max_strength = -1
        max_extension = None
        for extension in extensions:
            strength = class_name.count(extension) - extension.count(class_name[1:])
            # if the strength is negative, it means the extension is not a substring of the class_name
            if strength >= 0:
                max_strength = max(max_strength, strength)
                max_extension = extension
        # return the strongest extension
        return ".".join([class_name, max_extension, max_strength])
    # return the class name if the extension is not found
    return class_name
