
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
    # Iterate through the list of extensions
    for ext in extensions:
        # Get the strength of the extension
        strength = ext.count('E') - ext.count('e')
        # If the strength is greater than the current strongest extension, update it
        if strength > current_strength:
            current_strength = strength
            current_name = class_name + '.' + ext
        # If the strength is less than the current strongest extension, or the 
        # strength is the same, append it to the list
        else:
            strong_extensions.append(current_name)
    # Return the strongest extension as a string
    return '.' + class_name + '.' + strong_extensions[0]