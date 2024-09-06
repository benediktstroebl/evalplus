
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
    extensions_strength = {}
    for extension in extensions:
        num_upper = extension.upper().count('A')
        num_lower = extension.lower().count('a')
        extension_strength = num_upper - num_lower
        if extension_strength not in extensions_strength:
            extensions_strength[extension_strength] = []
        extensions_strength[extension_strength].append(extension)
    if len(extensions_strength) == 0:
        return f'{class_name}.None'
    strongest = max(extensions_strength, key=extensions_strength.get)
    return f'{class_name}.{strongest
