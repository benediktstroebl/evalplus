
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
    # Check if the class name is passed correctly
    if class_name == "":
        return ""
    
    # Get the set of extensions
    ext_set = set(extensions)
    
    # Find the strongest extension by iterating through the set of extensions
    ext_list = [ext for ext in ext_set]
    max_strength = -1
    max_index = 0
    for i in range(len(ext_list)):
        strength = (len(ext_list[i]) - len(ext_list[i].lower()))
        if strength > max_strength:
            max_strength = strength
            max_index = i
    # If there are two or more extensions with the same strength, choose the one that comes first in the list
    if max_index > 0:
        return class_name + "." + extensions[max_index]
    else:
        return ""
