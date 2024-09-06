
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
    max_extension = ''
    # Maximum extension strength will be equal to the difference between uppercase
    # and lowercase letters
    max_extension_strength = 0

    # Iterate over the list of extensions
    for extension in extensions:
        # Convert the extension to lowercase and find the number of uppercase letters
        extension_upper = sum(1 for char in extension if char.isupper())
        # Find the number of lowercase letters in the extension
        extension_lower = sum(1 for char in extension if char.islower())
        # Calculate the strength of the extension
        extension_strength = extension_upper - extension_lower
        # If the extension's strength is greater than the current maximum strength
        if extension_strength > max_extension_strength:
            # Update the maximum extension and its strength
            max_extension = extension
            max_extension_strength = extension_strength
    return class_name + '.' + max_extension

