
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
    # Sort the list of extensions by strength
    sorted_extensions = sorted(extensions, key=lambda x: (-len(x.split(".")), x))

    # Check if there are multiple extensions with the same strength
    if len(sorted_extensions) == 1:
        return class_name + "." + sorted_extensions[0]

    # If there are multiple extensions with the same strength, choose the first one
    extension_with_strength = sorted_extensions[0]
    for ext in sorted_extensions[1:]:
        if len(ext.split(".")) - len(extension_with_strength.split(".")) > 0:
            extension_with_strength = ext
            break
    return class_name + "." + extension_with_strength
