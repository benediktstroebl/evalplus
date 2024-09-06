
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
    strength = 0
    class_name = class_name[0:len(class_name)-len(class_name.split('.')[-1])]
    for extension in extensions:
        temp = extension[0:len(extension)-len(extension.split('.')[-1])]
        strength = strength + (len(extension)-len(temp))
    if strength == 0:
        return "{}.{}".format(class_name, extensions[0])
    elif strength > 0:
        return "{}.{}".format(class_name, extensions[extensions.index(max(extensions, key=len))])
    else:
        return
