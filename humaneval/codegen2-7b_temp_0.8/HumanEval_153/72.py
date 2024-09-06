
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
    class_name_patt = r"^[A-Z][A-Za-z0-9]+$"
    assert re.match(class_name_patt, class_name)

    strength_list = []
    for extension in extensions:
        extension_patt = r"^[A-Z][A-Za-z0-9]+$"
        assert re.match(extension_patt, extension)

        strength = len(extension) - len(extension.lower())

        strength_list.append((extension, strength))

    class_strength = max(strength_list)
    return "{}.{}.{}".format(class_name, class_strength[0], class_strength[1
