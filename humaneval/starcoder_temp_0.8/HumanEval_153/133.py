
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
    strength_dict = {}
    strongest_strength = -1
    strongest_extension = ''
    for extension in extensions:
        CAP = 0
        SM = 0
        for i in extension:
            if i.isupper():
                CAP += 1
            else:
                SM += 1
        strength = CAP - SM
        if strength in strength_dict.keys():
            strength_dict[strength].append(extension)
        else:
            strength_dict[strength] = [extension]
        if strength > strongest_strength:
            strongest_strength = strength
            strongest_extension = extension
    if len(strength_dict[strongest_strength]) == 1:
        return '{0}.{1}'.format(class_name, strongest_extension)
    else:
        for extension in strength_dict[strongest_strength]:
            if extension < strongest_extension:
                return '{0}.{1}'.format(class_name, extension)
