
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

    CAP = 0
    SM = 0
    for i in class_name:
        if i.isupper():
            CAP += 1
        else:
            SM += 1
    strength = float(CAP - SM) / (CAP + SM)
    result = class_name + '.' + extensions[0]
    for extension in extensions:
        temp = 0
        for i in extension:
            if i.isupper():
                temp += 1
            else:
                temp += 0
        strength_temp = float(CAP - SM) / (CAP + SM)
        if strength_temp == strength:
            if extension < result:
                result = extension + '.' + extensions[0]
        elif strength_temp > strength:
            strength = strength_temp
            result = extension + '.' + extensions[0]
    return result
