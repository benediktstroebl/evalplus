
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

    def is_uppercase(char):
        return char >= 'A' and char <= 'Z'
    def get_uppercase_count(string):
        uppercase_count = 0
        for char in string:
            if is_uppercase(char):
                uppercase_count += 1
        return uppercase_count
    def get_lowercase_count(string):
        lowercase_count = 0
        for char in string:
            if not is_uppercase(char):
                lowercase_count += 1
        return lowercase_count
    class_extension_strength = 0
    for extension in extensions:
        extension_strength = get_uppercase_count(extension) - get_lowercase_count(extension)
        if extension_strength > class_extension_strength:
            class_extension_strength = extension_strength
            extension_name = extension
    return class_name + '.' + extension_name
