
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

    import string
    cap = sum(map(lambda x: x in string.ascii_uppercase, class_name))
    sm = sum(map(lambda x: x in string.ascii_lowercase, class_name))
    extension = extensions[0]
    for i in extensions:
        cap_extension = sum(map(lambda x: x in string.ascii_uppercase, i))
        sm_extension = sum(map(lambda x: x in string.ascii_lowercase, i))
        if abs(cap_extension - sm_extension) < abs(cap - sm):
            extension = i
            cap = cap_extension
            sm = sm_extension
    return class_name + "." + extension


