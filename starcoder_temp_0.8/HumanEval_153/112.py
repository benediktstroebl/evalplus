
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
    # Create a dictionary of the extensions.
    extensions_dict = {}
    # Iterate through each extension and store each extension in a dictionary.
    for i in extensions:
        extensions_dict[i] = len(i)
    # Create a list of the strengths of the extensions.
    strength_list = []
    for j in extensions:
        # Create an integer to hold the strength value for the extension.
        strength = 0
        # Iterate through the length of the extension and add a strength value for each uppercase letter to the strength variable.
        for k in range(0, len(j)):
            if j[k].isupper():
                strength += 1
            # Subtract the strength for each lowercase letter from the strength variable.
            elif j[k].islower():
                strength -= 1
        # Add the strength value to the strength list.
        strength_list.append(strength)
    # Find the strength value that is the highest in the strength list.
    strength = max(strength_list)
    # Find the strongest extension in the extensions_dict.
    strongest_ext = ""
    for key, value in extensions_dict.items():
        if value == strength:
            strongest_ext = key
            break
    # Create the return string with the class name and the strongest extension.
    return class_name + "." + strongest_ext
