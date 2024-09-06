
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

    if class_name == "":
        return ""
    if extensions == []:
        return ""
    if len(extensions) == 0:
        return ""
    if len(extensions) == 1:
        return class_name + "." + extensions[0]

    strongest = 0
    strongest_extension = extensions[0]

    for i in extensions:
        n_caps = 0
        n_small = 0
        for j in i:
            if j.isupper():
                n_caps += 1
            else:
                n_small += 1
        strength = n_caps - n_small
        if strength > strongest:
            strongest = strength
            strongest_extension = i

    return class_name + "." + strongest_extension
