
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
    strength_list = []
    for ext in extensions:
        num_upper = sum(1 for c in ext if c.isupper())
        num_lower = sum(1 for c in ext if c.islower())
        strength = num_upper - num_lower
        strength_list.append([ext, strength])
    strength_list.sort(key=lambda x: x[1], reverse=True)
    if strength_list[0][1] == strength_list[1][1]:
        return class_name + '.' + strength_list[0][0]
    return class_name + '.' + strength_list[0][0]
