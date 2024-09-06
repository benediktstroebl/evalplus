
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
    extension_name = extensions[0]
    extension_strength = 0
    extension_strength_tuple = (extension_name.count('A'), extension_name.count('b'), extension_name.count('c'))
    for ext in extensions[1:]:
        extension_strength += abs(extension_strength_tuple[0] - ext.count('A') + extension_strength_tuple[1] - ext.count('b') + extension_strength_tuple[2] - ext.count('c'))
        if extension_strength > max(extension_strength):
            max_strength = extension_strength
            max_strength_extension = extension_name
            extension_strength = 0
            extension_strength_tuple = (extension_name.count('A'), extension_name.count('b'), extension_name.count('c'))
    return max_strength_extension
