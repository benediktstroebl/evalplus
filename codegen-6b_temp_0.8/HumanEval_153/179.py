
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
    def get_upper_and_lower_letters(extension):
        n_upper_letters = sum(1 for letter in extension if letter.isupper())
        n_lower_letters = sum(1 for letter in extension if letter.islower())
        return n_upper_letters - n_lower_letters
    strength_map = dict()
    for extension in extensions:
        strength = get_upper_and_lower_letters(extension)
        if strength not in strength_map or extension < strength_map[strength]:
            strength_map[strength] = extension
    
    return "{0}.{1}".format(class_name, strength_map[max(strength_map)])
