
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
    # create a set to keep track of used extensions
    used_extensions = set()
    # start by trying the first extension
    strongest_extension = None
    max_strength = -1
    for extension in extensions:
        # check if the extension is already used
        if extension in used_extensions:
            continue
        # update the strength
        strength = len(extension) - len(extension.lower())
        # update the strongest extension and the maximum strength
        if strength > max_strength:
            strongest_extension = extension
            max_strength = strength
    # if there is only one extension, just return it
    if not strongest_extension:
        return 'ClassName' + '.' + max_strength
    # otherwise, append it to the used extensions and try the next one
    used_extensions.add(strongest_extension)
    for next_extension in extensions:
        # check if the next extension is not used
        if next_extension not in used_extensions:
            # if the next extension has the same strength, update the strongest
            # extension and the maximum strength
            if len(next_extension) - len(next_extension.lower()) == max_strength:
                strongest_extension = next_extension
                max_strength = len(next_extension) - len(next_extension.lower())
            # if the next extension is stronger, update the strongest extension and
            # the maximum strength
            elif strength > max_strength:
                strongest_extension = next_extension
                max_strength = strength
    # if there are two or more extensions with the same strength, return the one
    # that comes first in the list
    if max_strength > 0:
        return 'ClassName' + '.' + max_strength
    return 'ClassName'