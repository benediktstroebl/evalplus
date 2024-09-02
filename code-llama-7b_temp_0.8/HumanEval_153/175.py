
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
    # 1. Count the number of lowercase letters in each extension
    lower_list = [len([i for i in ext if i.islower()]) for ext in extensions]

    # 2. Count the number of uppercase letters in each extension
    upper_list = [len([i for i in ext if i.isupper()]) for ext in extensions]

    # 3. Compute strength
    strength = [upper_list[i] - lower_list[i] for i in range(len(upper_list))]

    # 4. Return the strongest extension
    idx = strength.index(max(strength))
    return class_name + "." + extensions[idx]
