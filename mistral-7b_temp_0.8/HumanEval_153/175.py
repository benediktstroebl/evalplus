
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
    if len(extensions) == 0:
        return class_name
    extension_strengths = {str(x): 0 for x in extensions}
    for extension in extensions:
        extension_strengths[extension] = len([x for x in extension if x.isupper()]) - len([x for x in extension if x.islower()])
    extension_names = [extension for extension in extensions if extension_strengths[extension] != 0]
    extension_strengths = {str(x): extension_strengths[x] for x in extension_names}
    return class_name + "." + max(extension_strengths.items(), key=lambda x: x[1])[0]
