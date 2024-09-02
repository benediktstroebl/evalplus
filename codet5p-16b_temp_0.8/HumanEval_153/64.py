
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

    class_name_cap = 0
    class_name_sm = 0
    for x in class_name:
        if x.isupper():
            class_name_cap += 1
        else:
            class_name_sm += 1
    for x in extensions:
        ext_cap = 0
        ext_sm = 0
        for y in x:
            if y.isupper():
                ext_cap += 1
            else:
                ext_sm += 1
        if ext_cap - ext_sm > class_name_cap - class_name_sm:
            return class_name + '.' + x
    return ''
