
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
    class_name_caps = 0
    class_name_smalls = 0
    for i in class_name:
        if i.isupper():
            class_name_caps += 1
        else:
            class_name_smalls += 1
    max_extension = []
    for extension in extensions:
        extension_caps = 0
        extension_smalls = 0
        for j in extension:
            if j.isupper():
                extension_caps += 1
            else:
                extension_smalls += 1
        if (extension_caps - extension_smalls) > (class_name_caps - class_name_smalls) or (extension_caps - extension_smalls) == (class_name_caps - class_name_smalls) and extension < max_extension:
            max_extension = extension
    return class_name + '.' + max_extension

