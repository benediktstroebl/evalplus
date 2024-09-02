
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
    # This is the list of extensions that you have given,
    # this list should have the form ['ext1', 'ext2', ... , 'extn']
    ext_list = list(extensions)
    # Initialize the current extension as the first extension
    current_extension = ext_list[0]
    # Initialize the current strength to 0
    current_strength = 0
    # Iterate over the list of extensions
    for i in range(1, len(ext_list)):
        # Get the current extension
        ext = ext_list[i]
        # Get the strength of the current extension
        strength = len(ext)
        # Check if the current strength is stronger
        if strength > current_strength:
            # If it is stronger, update the current extension
            current_extension = ext
            current_strength = strength
    # return the classname with the strongest extension
    return class_name + '.' + current_extension
