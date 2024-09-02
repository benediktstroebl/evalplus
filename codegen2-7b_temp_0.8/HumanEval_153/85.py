
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
    strongest = ''
    for extension in extensions:
        ext_len = len(extension)
        cap_count = extension.upper().count('A')
        cap_count = cap_count + extension.upper().count('E')
        cap_count = cap_count + extension.upper().count('I')
        cap_count = cap_count + extension.upper().count('O')
        cap_count = cap_count + extension.upper().count('U')
        
        sm_count = extension.lower().count('a')
        sm_count = sm_count + extension.lower().count('e')
        sm_count = sm_count + extension.lower().count('i')
        sm_count = sm_count + extension.lower().count('o')
        sm_count = sm_count + extension.lower().count('u')
        
        strength = cap_count - sm_count
        if strength > strength:
            strongest = extension
            strength = strength
    return class_name + '.' + strongest
