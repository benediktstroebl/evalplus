
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
    from itertools import product
    cap, sm = 0, 0
    for i, j in product(class_name, extensions):
        if i.isupper():
            cap += 1
        else:
            sm += 1
    max_strength = cap - sm
    i, j = extensions[0], extensions[0]
    for k, l in product(extensions, extensions):
        if max_strength == cap - sm:
            if k[0].isupper():
                cap += 1
            else:
                sm += 1
            if max_strength == cap - sm:
                if len(i) > len(j):
                    i, j = j, i
                elif len(i) == len(j):
                    if i > j:
                        i, j = j, i
    return class_name + '.' + i
