
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

    import string
    UPPERCASE_LETTERS = [letter for letter in string.ascii_uppercase]
    LOWERCASE_LETTERS = [letter for letter in string.ascii_lowercase]
    
    class_name_upper = class_name.upper()
    class_name_lower = class_name.lower()
    
    if class_name_upper in UPPERCASE_LETTERS:
        SM = 0
        CAP = len(extensions)
    elif class_name_lower in LOWERCASE_LETTERS:
        SM = 0
        CAP = len(extensions)
    else:
        SM = 0
        for i in extensions:
            SM += i.lower().count(' ') + 1
        CAP = len(extensions)
    strength = CAP - SM
    return class_name+"."+extensions[strength].strip()
