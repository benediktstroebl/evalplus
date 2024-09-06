
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
    extensions.sort()
    highest_strength = 0
    highest_strength_index = 0
    for index, extension in enumerate(extensions):
        name = extension.split('.')
        uppercase = sum(1 for c in name[-1] if c.isupper())
        lowercase = sum(1 for c in name[-1] if c.islower())
        strength = uppercase - lowercase
        if strength > highest_strength:
            highest_strength = strength
            highest_strength_index = index
    return "{0}.{1}".format(class_name, extensions[highest_strength_index])

