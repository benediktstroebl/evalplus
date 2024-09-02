
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
    if class_name == '' or class_name == None:
        return None

    class_strength = 0

    for extension in extensions:
        class_name_strength = extension.count(class_name)
        extension_strength = extension.count('.' + extension)

        if class_name_strength > class_strength:
            class_name = extension
            class_strength = class_name_strength
        elif class_name_strength == class_strength:
            if extension_strength > class_strength:
                class_name = extension
                class_strength = extension_strength

    return class_name + '.' + class_name.upper()
