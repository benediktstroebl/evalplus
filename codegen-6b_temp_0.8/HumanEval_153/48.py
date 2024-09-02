
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
    from collections import Counter
    matching = []
    for extension in extensions:
        extension_name = extension.split('.')[-1].upper()
        strength = sum(1 for letter in extension_name if letter.isupper()) - \
            sum(1 for letter in extension_name if letter.islower())
        matching.append(tuple([strength, extension]))
    strength = max(matching, key=lambda tup: tup[0])[0]
    for extension in matching:
        if extension[0] == strength:
            return "{0}.{1}".format(class_name, extension[1])

