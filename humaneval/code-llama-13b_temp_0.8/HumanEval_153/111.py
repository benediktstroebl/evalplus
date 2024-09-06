
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
    # your code here
    cap = 0
    capp = 0
    sm = 0
    smp = 0
    cap_str = ''
    sm_str = ''
    for i in extensions:
        for j in i:
            if j.isupper():
                cap = cap + 1
                cap_str = cap_str + j
            elif j.islower():
                sm = sm + 1
                sm_str = sm_str + j
        if cap - sm > capp - smp:
            capp = cap
            smp = sm
            sm_str = ''
            cap_str = ''
            cap = 0
            sm = 0
        elif cap - sm < capp - smp:
            cap = 0
            sm = 0
        else:
            capp = cap
            smp = sm
            sm_str = ''
            cap_str = ''
            cap = 0
            sm = 0
    return class_name + '.' + extensions[extensions.index(cap_str)]

