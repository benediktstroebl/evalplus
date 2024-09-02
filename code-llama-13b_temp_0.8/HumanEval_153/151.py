
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
    cap = 0
    for i in extensions:
        for j in i:
            if j.isupper():
                cap += 1
    sm = 0
    for i in extensions:
        for j in i:
            if j.islower():
                sm += 1
    cap_list = []
    sm_list = []
    for i in extensions:
        cap_list.append(cap - sm)
        sm_list.append(sm)
    max_cap = max(cap_list)
    min_sm = min(sm_list)
    i = 0
    while i < len(cap_list):
        if cap_list[i] == max_cap and sm_list[i] == min_sm:
            return class_name + "." + extensions[i]
        i += 1

