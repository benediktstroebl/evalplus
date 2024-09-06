
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

    # find the strongest extension and return a string in this 
    # format: ClassName.StrongestExtensionName

    if len(extensions) == 0:
        return class_name

    strongest_ext = extensions[0]
    strongest_ext_strength = - extensions[0].lower().count("a") + extensions[0].lower().count("e") + extensions[0].lower().count("i") + extensions[0].lower().count("o") + extensions[0].lower().count("u")

    for i in range(1, len(extensions)):
        current_ext_strength = - extensions[i].lower().count("a") + extensions[i].lower().count("e") + extensions[i].lower().count("i") + extensions[i].lower().count("o") + extensions[i].lower().count("u")
        if current_ext_strength > strongest_ext_strength:
            strongest_ext_strength = current_ext_strength
            strongest_ext = extensions[i]

    return f"{class_name}.{strongest_ext}"

