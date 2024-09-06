
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
    # check if the list of extensions is not empty
    if len(extensions) == 0:
        return class_name
    
    # sort the list of extensions by strength
    extensions = sorted(extensions, key=lambda x: -x[1], reverse=True)
    
    # check if there are two or more extensions with the same strength
    if len(extensions) == 1:
        return class_name + '.' + extensions[0]
    
    # find the strongest extension
    extension = extensions[0]
    strength = extension[1]
    i = 1
    while i < len(extensions) and extensions[i][1] == strength:
        i += 1
    if i == len(extensions):
        return class_name + '.' + extensions[0]
    else:
        return class_name + '.' + extensions[i]
