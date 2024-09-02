
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
    import string
    class_name = class_name.lower()
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    extensions_list = [s for s in extensions]
    extensions_list.sort()
    max_strength = -9999999999999
    strong_extension = ''
    for extension in extensions_list:
        extension = extension.lower()
        if len(set(extension).intersection(uppercase_letters)) > len(set(extension).intersection(lowercase_letters)):
            strength = len(set(extension).intersection(uppercase_letters)) - len(set(extension).intersection(lowercase_letters))
        else:
            strength = 0
        if strength > max_strength:
            max_strength = strength
            strong_extension = extension
    return class_name + '.' + strong_extension
