
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
    # your code here
    x = 0
    z = 0
    l = len(extensions)
    y = extensions[x].lower()
    b = extensions[x].upper()
    c = len(y)
    d = len(b)
    for i in range(l):
        if z != 0:
            z = 0
        y = extensions[i].lower()
        b = extensions[i].upper()
        c = len(y)
        d = len(b)
        x += 1
        if d - c > z:
            z = d - c
            if z == 0:
                z = c - d
    return class_name + '.' + extensions[x - 1]

