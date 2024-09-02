
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
    max_strength = -1
    max_strength_index = -1
    for extension in extensions:
        strength = -1
        strength_index = -1
        for i in range(len(extension)):
            if extension[i].isupper() and len(extension) > i:
                strength = int(extension[i])
                strength_index = i
                break
        if strength > max_strength:
            max_strength = strength
            max_strength_index = strength_index
    if max_strength == -1 or max_strength_index == -1:
        return class_name
    else:
        return '%s.%s' % (class_name, extensions[max_strength_index])