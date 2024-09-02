
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
    class_name_upper = len(class_name) - sum(1 for i in class_name if i.isupper())
    class_name_lower = len(class_name) - sum(1 for i in class_name if i.islower())
    strongest_extension = max(extensions, key = lambda extension: len(extension) - sum(1 for i in extension if i.isupper()) - sum(1 for i in extension if i.islower()))
    strongest_extension_upper = len(strongest_extension) - sum(1 for i in strongest_extension if i.isupper())
    strongest_extension_lower = len(strongest_extension) - sum(1 for i in strongest_extension if i.islower())
    if strongest_extension_upper - strongest_extension_lower == class_name_upper - class_name_lower:
        return class_name + '.' + extensions[0]
    else:
        return class_name + '.' + strongest_extension

