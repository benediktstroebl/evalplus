
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
    strings = []
    for extension in extensions:
        string = extension.split('.')
        strings.append(string[1])
    strings.sort()
    strings = ".".join(strings)
    length = len(strings)
    if length < 2:
        return string
    if strings[0].isupper():
        return string
    elif strings[0].islower():
        first = strings[0]
        second = strings[1]
        for i in range(length):
            if strings[i].isupper():
                return string
            else:
                second = strings[i]
        return string + "." + first + second
    else:
        return string + "." + strings[1]
