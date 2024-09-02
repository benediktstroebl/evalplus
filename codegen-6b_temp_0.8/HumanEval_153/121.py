
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
    class_strength = {
        'A': 0,
        'B': 0,
        'C': 0
    }

    for extension in extensions:
        extension = extension.lower()
        for character in extension:
            if character in string.ascii_lowercase:
                class_strength[character] = class_strength[character] + 1

    for key in class_strength:
        class_strength[key] = class_strength[key] - len(class_name)
    
    max_strength = max(class_strength.values())
    extensions_list = []
    for key in class_strength:
        if class_strength[key] == max_strength:
            extensions_list.append(class_name + '.' + key)

    return extensions_list[0]
