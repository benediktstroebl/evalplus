
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
    dic_name_extension_strength = {}
    dic_name_strength = {}
    for extension in extensions:
        strength = len(extension) - sum(1 for x in extension if x.isupper()) - sum(1 for x in extension if x.islower())
        dic_name_extension_strength[extension] = strength
        dic_name_strength[extension] = strength
    print(f"Class {class_name}'s strongest extension is: {class_name}.{max(dic_name_extension_strength, key=dic_name_extension_strength.get)}")


