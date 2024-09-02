
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
    # Your code here
    names = []
    for extension in extensions:
        names.append(extension.capitalize())
    class_strength = 0
    extension_strength = 0
    for i in range(len(names)):
        if names[i][0] == names[i][0].upper() and names[i][1] == names[i][1].lower():
            class_strength += 1
        else:
            class_strength += 0
        if names[i][1] == names[i][1].upper() and names[i][0] == names[i][0].lower():
            extension_strength += 1
        else:
            extension_strength += 0
    if class_strength >= extension_strength:
        return class_name.capitalize() + ". " + extensions[0]
    else:
        for i in range(len(extensions)):
            if extensions[i].capitalize() == extensions[0].capitalize():
                pass
            else:
                return class_name.capitalize
