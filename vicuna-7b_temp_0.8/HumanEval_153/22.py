
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
    strongest_extension = None
    best_strength = -1
    for extension in extensions:
        # Get the strength of the extension
        extension_strength = -1
        if len(extension) > 0:
            extension_strength = len(extension) - len(extension.lower())
        # Find the strongest extension
        for i in range(len(extensions)):
            if extensions[i].lower() > extensions[i+1].lower():
                extension_strength = -1
                break
        # If there are two or more extensions with the same strength, choose the one that comes first
        if extension_strength != best_strength:
            if extension_strength > best_strength:
                strongest_extension = '.'.join([class_name, extension])
                best_strength = extension_strength
        elif extension_strength == best_strength:
            strongest_extension = '.'.join([class_name, extension])
        if extension_strength > best_strength:
            best_strength = extension_strength
    return strongest_extension
