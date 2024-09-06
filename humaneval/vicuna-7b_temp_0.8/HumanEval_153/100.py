
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
    class_name_split = class_name.split('.')
    for extension in extensions:
        extension_split = extension.split('.')
        for i in range(len(extension_split)):
            cap = len(class_name_split[i].upper())
            sm = len(extension_split[i].lower())
            ratio = cap - sm
            if ratio > 0:
                return class_name_split[0] + '.' + extension_split[i] + '.' + class_name_split[1:][1:] + '.' + extension_split[i+1:len(extension_split)][1:] + '.' + extension_split[i] + '.' + class_name_split[1]
    return class_name
