
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
    # Find the strongest extension
    max_strength = -1
    max_index = -1
    for i, ext in enumerate(extensions):
        strength = len(ext) - len(ext.lower())
        if strength > max_strength:
            max_strength = strength
            max_index = i
    # If there are two or more extensions with the same strength, 
    # choose the one that comes first in the list
    if max_index == -1 or (max_index + 1) in [idx for idx, ext in enumerate(extensions) if len(ext) - len(ext.lower()) == max_strength]:
        return class_name + "." + extensions[max_index]
    else:
        return class_name + "." + extensions[max_index + 1] if max_index < len(extensions) - 1 else class_name + "." + extensions[0]
