
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
    sm = 0
    for i in range(len(class_name)):
        if class_name[i].isupper():
            cap += 1
        if class_name[i].islower():
            sm += 1
    strongest_extension = class_name + '.' + class_name.capitalize() + '.' + class_name.lower()
    for extension in extensions:
        cap_ext = 0
        sm_ext = 0
        for i in range(len(extension)):
            if extension[i].isupper():
                cap_ext += 1
            if extension[i].islower():
                sm_ext += 1
        if (cap - sm) / (cap_ext - sm_ext) > (cap - sm) / (cap_ext - sm_ext):
            strongest_extension = class_name + '.' + extension
    return strongest_extension
