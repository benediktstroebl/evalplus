
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
    if type(extensions) == list:
        extensions = [i.replace(' ', '') for i in extensions]
        if len(extensions) == 0:
            return class_name
        strength_list = []
        for i in extensions:
            strength_list.append((len([j for j in i if j.isupper()]), len([j for j in i if j.islower()])))
        if strength_list.count(max(strength_list)) > 1:
            return class_name + '.' + sorted(extensions, key=lambda x: x[0] - x[1])[0]
        else:
            return class_name + '.' + max(strength_list, key=lambda x: x[0] - x[1])[2]
    else:
        raise TypeError

