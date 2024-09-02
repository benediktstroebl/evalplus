
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
    for extension in extensions:
        extension_strength[extension] = 0
        for i in range(len(extension)):
            if extension[i].isupper():
                extension_strength[extension] += 1
            else:
                extension_strength[extension] -= 1
    
    strongest_extension = None
    for extension, strength in extension_strength.items():
        if strongest_extension is None or strength > extension_strength[strongest_extension]:
            strongest_extension = extension
    
    strongest_extension_name = None
    for extension in extensions:
        if extension == strongest_extension:
            strongest_extension_name = '.' + class_name + strongest_extension
    return class_name + strongest_extension_name
