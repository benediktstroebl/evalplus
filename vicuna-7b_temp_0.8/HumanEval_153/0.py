
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
    # This will keep track of the number of uppercase and lowercase letters
    upper_count = 0
    lower_count = 0
    # Iterate over the list of extensions
    for extension in extensions:
        # Get the strength of the extension
        extension_strength = len(extension.upper()) - len(extension.lower())
        # Update the number of uppercase and lowercase letters
        upper_count += extension_strength
        lower_count -= extension_strength
    # Find the extension with the highest strength
    strongest_extension = extensions[0]
    while all([extension_strength > strongest_extension_strength,
              extension_strength > 0] for extension in extensions):
        # Update the strength of the strongest extension
        strongest_extension_strength += 1
        strongest_extension = extensions.pop(0)
    # Return the strongest extension as the desired class name
    return class_name + '.' + strongest_extension.lower() + '.' + 'StrongestExtension'
