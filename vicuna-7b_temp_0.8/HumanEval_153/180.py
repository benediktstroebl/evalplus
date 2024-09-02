
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
    # Initialize the strongest extension and its strength
    strongest_extension = None
    strongest_strength = -1
    for ext in extensions:
        # Calculate the strength
        cap = len(ext.upper())
        sm = len(ext.lower())
        strength = cap - sm
        # Check if the strength is better than the current strongest
        if strength > strongest_strength:
            strongest_extension = ext
            strongest_strength = strength
    # Check if the current extension is the same as the previous one
    if strongest_extension is not None:
        return strongest_extension + '.' + strongest_extension.lower()
    # If there are two or more extensions with the same strength, return the first one in the list
    return strongest_extension