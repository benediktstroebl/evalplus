
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
    # Split the extension argument into a list of strings
    for extension in extensions:
        # Split the extension into a list of letters
        extension_letters = list(extension)
        # If the extension is only made of letters, append an empty string
        if len(extension_letters) == 0:
            extension_letters = ['']
        # Find the letter count for the extension
        extension_count = 0
        for letter in extension_letters:
            if letter.isupper():
                extension_count += 1
            elif letter.islower():
                extension_count += 1
            elif letter == ' ':
                extension_count += 1
        # Find the length of the extension
        extension_length = len(extension)
        # Find the strength of the extension
        extension_strength = extension_count - extension_length
        # If the extension is the strongest so far, store it
        if extension_strength > strongest_extension_strength:
            strongest_extension_name = extension
            strongest_extension_strength = extension_strength
    # Return the class name + the strongest extension
    return "{0}.{1}".format(class_name, strongest_extension_name)

