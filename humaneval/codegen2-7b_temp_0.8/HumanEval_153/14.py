
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
    strongest = extensions[0]
    for i in range(len(extensions)):
        strength = strength - len(extensions[i])
        for j in range(len(extensions[i])):
            strength = strength + (1 if extensions[i][j].isupper() else 0) - (1 if extensions[i][j].islower() else 0)
            if strength > strength_of_strongest:
                strength_of_strongest = strength
                strongest = extensions[i]
    return "%s.%s" % (class_name, strongest
