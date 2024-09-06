
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

    def convert_string(str):
        return ''.join([x if x.islower() else x.upper() for x in str])
    class_name_str = convert_string(class_name)
    class_strength = 0
    for ext in extensions:
        ext_str = convert_string(ext)
        ext_CAP = sum([x.isupper() for x in ext_str])
        ext_SM = sum([x.islower() for x in ext_str])
        strength = ext_CAP - ext_SM
        if strength > class_strength:
            class_strength = strength
            strongest_extension = ext
    return class_name_str + '.' + strongest_extension
