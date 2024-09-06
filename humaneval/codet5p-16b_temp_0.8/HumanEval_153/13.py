
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

    strength = 0
    for ext in extensions:
        num_upper = 0
        num_lower = 0
        for i in ext:
            if i.isupper():
                num_upper += 1
            else:
                num_lower += 1
        if num_upper == 0 or num_lower == 0:
            strength += 0
        else:
            strength += (num_upper - num_lower) / len(ext)
    strength = str(round(strength, 2))
    return class_name + '.' + '.'.join(extensions).split('.')[-1] + '.' + strength + '.'

