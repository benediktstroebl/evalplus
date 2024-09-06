
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

    max_cap = 0
    max_cap_index = 0
    max_sm = 0
    max_sm_index = 0

    for i in range(0, len(extensions)):
        cap = 0
        sm = 0
        for j in range(0, len(extensions[i])):
            if extensions[i][j].isupper():
                cap += 1
            if extensions[i][j].islower():
                sm += 1

        if (cap - sm) > max_cap:
            max_cap = cap - sm
            max_cap_index = i

        if (cap - sm) < max_sm:
            max_sm = cap - sm
            max_sm_index = i

    return class_name + '.' + extensions[max_cap_index]
    

