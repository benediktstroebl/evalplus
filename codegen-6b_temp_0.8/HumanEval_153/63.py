
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
    strength = {}
    for ext in extensions:
        string_ext = ext[0].upper() + ext[1:].lower()
        for letter in string_ext:
            if letter.isupper():
                strength[letter] = strength.setdefault(letter, 0) + 1
            elif letter.islower():
                strength[letter] = strength.setdefault(letter, 0)

    max_strength = 0
    max_extension = None
    for ext in extensions:
        strength_ = 0
        for letter in ext[0].upper() + ext[1:].lower():
            if letter.isupper():
                strength_ += 1
            elif letter.islower():
                strength_ += -1
        if strength_ > max_strength:
            max_strength = strength_
            max_extension = ext

    return '{}.{}'.format(class_name, max_extension)
