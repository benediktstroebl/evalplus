
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
    upper_class = [x for x in class_name if x.isupper()]
    lower_class = [x for x in class_name if x.islower()]
    cap_class = len(upper_class)
    sm_class = len(lower_class)
    strength_class = cap_class - sm_class
    for extension in extensions:
        upper_extension = [x for x in extension if x.isupper()]
        lower_extension = [x for x in extension if x.islower()]
        cap_extension = len(upper_extension)
        sm_extension = len(lower_extension)
        strength_extension = cap_extension - sm_extension
        if strength_extension > strength_class:
            return class_name + '.' + extension
    return class_name + '.' + extensions[0]
    
