
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
    if len(extensions) == 0:
        return class_name
    strength = 0
    for extension in extensions:
        if len(extension) == 1:
            letters = ''.join(reversed(extension))
            cap = sum(ord(c) - ord('A') + 1 for c in letters)
            sm = sum(ord(c) - ord('a') + 1 for c in letters)
            strength = cap - sm
            break
        else:
            extension_name = '.'.join(extension)
            cap = len(extension_name)
            sm = len(extension)
            strength = cap - sm
    result = class_name + '.' + '.'.join(extensions) + '.' + extension_name
    while result in extensions:
        result = class_name + '.' + '.'.join(extensions[:-1]) + '.' + extension_name
    return result