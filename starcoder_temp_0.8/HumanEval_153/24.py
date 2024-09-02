
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
    names = [e.replace(class_name + '.', '') for e in extensions]
    cap = len([l for l in names if l.isupper()])
    low = len([l for l in names if l.islower()])
    strengths = [cap-low for l in names]
    # Find the strongest extension.
    strongest = max(strengths)
    # Find all the extensions with the strongest strength.
    strongest_extensions = [i for i, e in enumerate(strengths) if e == strongest]
    # Choose the first one.
    extension = strongest_extensions[0]
    # Return the extension.
    return class_name + '.' + names[extension]
