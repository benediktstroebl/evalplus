
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
    # extract the class name from class_name
    class_name = class_name.split('.')[-1]
    # find the strongest extension
    strongest_extension = None
    strongest_strength = -1
    for ext in extensions:
        # extract the extension name from the extension
        extension = ext.split('.')[-1]
        # calculate the strength of the extension
        strength = sum(len(part) - len(part.lower()) for part in extension.split('_'))
        # update the strongest extension and strength if necessary
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    if strongest_extension is None or len(extensions) == 0:
        return class_name
    else:
        return class_name + '.' + strongest_extension
