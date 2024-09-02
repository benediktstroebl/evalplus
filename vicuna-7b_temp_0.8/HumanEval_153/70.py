
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
    # Check if the class already has an extension
    if class_name in extensions:
        return class_name + '.' + extensions[class_name]
        
    # Find the strength of each extension
    strengths = []
    for ext in extensions:
        strengths.append(len(ext) * 1000000 + len(ext.split('.')))

    # Find the strongest extension by comparing the strengths
    strongest = sorted(str(s) for s in strengths)[0]

    # Find the class name by removing the strength and the period from the strongest extension
    class_name_str = class_name + '.' + strongest
    class_name = class_name_str.split('.')[-1]

    # Find the strongest extension name
    ext = strongest.split('.')[-1]
    ext_name = '.'.join(ext.split('.')[:-1])

    return class_name + '.' + ext_name + '.' + strongest