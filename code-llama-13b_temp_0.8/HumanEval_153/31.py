
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
    class_name_length = len(class_name)
    class_name_upper = 0
    class_name_lower = 0
    strongest_extension = []
    max_strength = 0
    for ext in extensions:
        if not strongest_extension:
            strongest_extension.append(ext)
        ext_length = len(ext)
        ext_upper = 0
        ext_lower = 0
        for i in range(ext_length):
            if ext[i].isupper():
                ext_upper += 1
            else:
                ext_lower += 1
        ext_strength = ext_upper - ext_lower
        if ext_strength > max_strength or (ext_strength == max_strength and ext < strongest_extension[0]):
            strongest_extension.clear()
            strongest_extension.append(ext)
            max_strength = ext_strength
    return class_name + '.' + strongest_extension[0]

