
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
    # Determine the upper and lower letters we need to use 
    upper = False
    lower = False
    for c in class_name:
        if c.isupper(): upper = True
        if c.islower(): lower = True
    # Loop through the extensions to find the strongest one
    strength = 0
    strongest = extensions[0]
    for ext in extensions:
        new_strength = 0
        # Do the same as in the exercise above
        for c in ext:
            if c.isupper(): new_strength += 1
            elif c.islower(): new_strength -= 1
        if new_strength > strength: 
            strength = new_strength
            strongest = ext
    # Return the class name and the strongest extension
    return '{0}.{1}'.format(class_name, strongest)


