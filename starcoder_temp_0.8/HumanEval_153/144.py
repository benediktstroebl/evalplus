
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
    class_name = class_name.lower()
    Strongest_Strength = 0
    Strongest_Extension_Name = ""
    for extension in extensions:
        strength = 0
        class_name_len = len(class_name)
        extension_len = len(extension)
        for i in range(class_name_len):
            if class_name[i].isupper() and extension[i].isupper():
                strength += 1
            elif class_name[i].islower() and extension[i].islower():
                strength -= 1
            elif class_name[i].isupper() and extension[i].islower():
                strength -= 10
            elif class_name[i].islower() and extension[i].isupper():
                strength += 10
        if strength > Strongest_Strength:
            Strongest_Strength = strength
            Strongest_Extension_Name = extension
    return class_name + "." + Strongest_Extension_Name
