
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
    temp = []
    extension = []
    # store each extension name in temp
    for item in extensions:
        temp.append(item)
    # get the extension with the highest strength and store it in extension
    for i in temp:
        if (ord(i[0]) > 97 and ord(i[0]) < 123) or (ord(i[0]) > 64 and ord(i[0]) < 91):
            extension.append(i)
    # compare the strength of all extension in extension and store the strongest one in extension
    for item in extension:
        if (item[0:1] == item[0:1].lower()) and (item[0:1] == item[0:1].upper()):
            extension.remove(item)
    if len(extension) == 0:
        return ""
    else:
        return class_name + "." + extension[0]
