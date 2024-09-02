
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

    print('sorting extensions')
    extensions = sorted(extensions, key = lambda x : len([c for c in x if c.isupper()]))
    print('extensions are:', extensions)
    
    max_strength = 0
    max_strength_name = None
    
    for ext in extensions:
        strength = len([c for c in ext if c.isupper()]) - len([c for c in ext if c.islower()])
        if strength == max_strength:
            max_strength_name = '.'.join([class_name, ext])
        elif strength > max_strength:
            max_strength = strength
            max_strength_name = '.'.join([class_name, ext])
    
    print('extension name: ', max_strength_name)
    print('max strength: ', max_strength)
    return max_strength_name
