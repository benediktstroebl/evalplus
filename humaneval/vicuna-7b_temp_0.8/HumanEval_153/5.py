
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
    # Check if the given class is valid
    if not issubclass(class_name, tuple):
        raise ValueError("Class name must be a valid Python class")
    
    # Sort the extensions by strength
    extensions.sort(key=lambda x: (-1 if x[0] == "E" else 0, -1 if x[1] == "S" else 0, -1 if x[2] == "I" else 0))
    
    # Check if there are any extensions with the same strength
    best_extension = None
    best_strength = -1
    for x in extensions:
        if x[0].isalpha() == x[1].isalpha() == x[2].isalpha() == False:
            # Extension contains only uppercase letters
            if best_extension is None or best_strength > x[0].count("E") - x[0].count("S") - x[0].count("I"):
                best_extension = x[0]
                best_strength = x[0].count("E") - x[0].count("S") - x[0].count("I")
        else:
            # Extension contains only lowercase letters
            if best_extension is None or best_strength > x[1].count("E") - x[1].count("S") - x[1].count("I"):
                best_extension = x[1]
                best_strength = x[1].count("E") - x[1].count("S") - x[1].count("I")
    
    # Return the strongest extension
    if best_extension is not None:
        return class_name + "." + best_extension + "." + class_name
    else:
        return class_name
