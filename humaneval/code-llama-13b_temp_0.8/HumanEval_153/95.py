
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
    # your code here
    class_name = class_name + '.'
    upper_class = len(class_name.upper())
    lower_class = len(class_name.lower())
    max_ratio = -100
    max_extension = ''
    for ext in extensions:
        upper_ext = len(ext.upper())
        lower_ext = len(ext.lower())
        ratio = (upper_ext - lower_ext)/(upper_class - lower_class)
        if ratio > max_ratio:
            max_ratio = ratio
            max_extension = ext
    return class_name + max_extension

