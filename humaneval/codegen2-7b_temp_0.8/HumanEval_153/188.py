
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
    extension_strength = {}
    for ext in extensions:
        ext = ext.split('.')
        extension_strength[ext[1]] = len(ext[0]) - len(ext[1])
    class_name = class_name.split('.')
    if max(extension_strength.values()) == min(extension_strength.values()):
        return class_name[0] + '.' + max(extension_strength, key=extension_strength.get) + '.' + class_name[1]
    return class_name[0] + '.' + min(extension_strength, key=extension_strength.get) + '.' + class_name[1]
