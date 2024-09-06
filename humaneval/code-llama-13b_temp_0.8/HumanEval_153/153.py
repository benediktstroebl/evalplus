
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
    class_name_uppercase = 0
    class_name_lowercase = 0
    for letter in class_name:
        if letter.isupper():
            class_name_uppercase += 1
        elif letter.islower():
            class_name_lowercase += 1
    strongest_extension = ''
    strongest_extension_strength = 0
    for extension in extensions:
        extension_uppercase = 0
        extension_lowercase = 0
        for letter in extension:
            if letter.isupper():
                extension_uppercase += 1
            elif letter.islower():
                extension_lowercase += 1
        strength = extension_uppercase - extension_lowercase
        if strength > strongest_extension_strength:
            strongest_extension = extension
            strongest_extension_strength = strength
    return class_name + '.' + strongest_extension

