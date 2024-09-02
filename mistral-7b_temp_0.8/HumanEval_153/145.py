
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
    class_name = class_name
    extensions = extensions
    for i in extensions:
        if len(i) == 0:
            pass
        elif len(i) == 1:
            if i[0] == "a" or i[0] == "A" or i[0] == "e" or i[0] == "E" or i[0] == "i" or i[0] == "I" or i[0] == "o" or i[0] == "O" or i[0] == "u" or i[0] == "U":
                pass
            else:
                extensions.remove(i)
    if len(extensions) == 0:
        pass
    else:
        strongest_extension = extensions[0]
        for j in extensions:
            if len(j) == len(strongest_extension):
                if j[0] == strongest_extension[0] and j[1] == strongest_extension[1] and j[2] == strongest_extension[2] and j[3] == strongest_extension[3] and
