
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
    extension_strength = {}
    for extension in extensions:
        letter_count = {}
        for letter in extension:
            if letter.isupper():
                letter_count[letter] = letter_count.get(letter, 0) + 1
        strength = sum([letter_count.get(letter, 0) for letter in extension]) - sum([letter_count.get(letter, 0) for letter in extension if letter.islower()])
        extension_strength[extension] = strength
    best_extension = max(extension_strength, key=extension_strength.get)
    return "{}.{}".format(class_name, best_extension)