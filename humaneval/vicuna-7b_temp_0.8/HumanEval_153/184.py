
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
    # Check if the class name is in the list
    if class_name in extensions:
        # Get the extensions
        extensions = extensions[class_name]
        # Get the list of extensions in the correct order
        extension_name_list = sorted(extensions, key=lambda x: x[1], reverse=True)
        # Find the strongest extension
        max_strength = 0
        max_index = 0
        for index, (name, strength) in enumerate(extension_name_list):
            # Convert the strength to a number
            strength_num = int(strength)
            # Check if the strength is positive
            if strength_num > 0:
                # Subtract the number of lowercase letters from the strength
                max_strength = max(max_strength, strength_num - len(name) - 1)
                # Update the maximum strength and index
                max_strength = max_strength if strength_num > max_strength else max_strength + 1
                max_index = index
        # Return the strongest extension
        return extension_name_list[max_index][0]
    else:
        return class_name
