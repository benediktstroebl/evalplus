
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
    class_name_upper = class_name.upper()
    class_name_lower = class_name.lower()
    strongest_extension = extensions[0]
    strongest_extension_up = strongest_extension.upper()
    strongest_extension_low = strongest_extension.lower()
    strongest_extension_strength = strongest_extension_up.count(strongest_extension) - strongest_extension_low.count(strongest_extension)
    for ext in extensions:
        ext_up = ext.upper()
        ext_low = ext.lower()
        ext_strength = ext_up.count(ext) - ext_low.count(ext)
        if ext_strength > strongest_extension_strength:
            strongest_extension = ext
            strongest_extension_up = ext_up
            strongest_extension_low = ext_low
            strongest_extension_strength = ext_strength
        elif ext_strength == strongest_extension_strength:
            if ext_low < strongest_extension_low:
                strongest_extension = ext
                strongest_extension_up = ext_up
                strongest_extension_low = ext_low
                strongest_extension_strength = ext_strength
    return class_name + '.' + strongest_extension
    
