
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
    class_name_ = class_name
    extension = []
    extension.append(extensions[0])
    extension.append(extensions[0].count('A'))
    extension.append(extensions[0].count('a'))
    extension.append(extension[1] - extension[2])
    for i in range(1, len(extensions)):
        if extensions[i] == extension[0]:
            extension.append(extensions[i])
        elif extensions[i].count('A') > extension[1]:
            extension[0] = extensions[i]
            extension[1] = extensions[i].count('A')
            extension[2] = extensions[i].count('a')
            extension[3] = extension[1] - extension[2]
            extension[4] = extensions[i]
        elif extensions[i].count('A') == extension[1]:
            if extensions[i].count('a') < extension[2]:
                extension[0] = extensions[i]
                extension[1] = extensions[i].count('A')
                extension[2] = extensions[i].count('a')
                extension[3] = extension[1] - extension[2]
                extension[4] = extensions[i]
            elif extensions[i].count('a') == extension[2]:
                extension.append(extensions[i])
    return class_name_ + '.' + extension[4]

