
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
    # put your code here
    res = None
    for e in extensions:
        if res != None:
            if ''.join([x.upper() for x in e]) > ''.join([x.upper() for x in res]):
                res = e
            elif ''.join([x.upper() for x in e]) == ''.join([x.upper() for x in res]):
                res = e
            else:
                continue
        else:
            if ''.join([x.upper() for x in e]) == ''.join([x.upper() for x in e]):
                res = e
            else:
                continue
    return '{}.{}'.format(class_name, res)
