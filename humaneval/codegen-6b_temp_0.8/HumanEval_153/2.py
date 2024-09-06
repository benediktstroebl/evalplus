
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
    #########################################
    #  Do not change anything before this  #
    #########################################

    # We'll need a dictionary for the extension to strength mapping
    extension_to_strength = {}

    # For each extension, compute its strength and store it in the
    # dictionary
    for extension in extensions:
        extension_strength = 0
        for character in extension:
            if character.isupper():
                extension_strength += 1
            elif character.islower():
                extension_strength -= 1

        extension_to_strength[extension] = extension_strength

    # Find the strongest extension and return its name
    strongest_extension = max(extension_to_strength, key=extension_to_strength.get)
    return "{}.{}".format(class_name, strongest_extension)
