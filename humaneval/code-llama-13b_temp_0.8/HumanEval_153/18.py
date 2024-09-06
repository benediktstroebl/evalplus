
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
    class_name_up = class_name.upper()
    class_name_low = class_name.lower()
    class_name_cap = len(class_name_up)
    class_name_sm = len(class_name_low)
    for i in range(len(extensions)):
        extensions_up = extensions[i].upper()
        extensions_low = extensions[i].lower()
        extensions_cap = len(extensions_up)
        extensions_sm = len(extensions_low)
        extensions_strength = extensions_cap - extensions_sm
        if class_name_cap >= class_name_sm:
            class_name_strength = class_name_cap - class_name_sm
        else:
            class_name_strength = class_name_sm - class_name_cap
        if extensions_strength > class_name_strength:
            return class_name + '.' + extensions[i]
    return class_name + '.' + extensions[0]
