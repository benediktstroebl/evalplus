
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
    
    output = ''
    extensions_lambda = [lambda e: e.count('A'), lambda e: e.count('a'), lambda e: e.count('E'), lambda e: e.count('e'), 
                         lambda e: e.count('I'), lambda e: e.count('i'), lambda e: e.count('O'), lambda e: e.count('o'),
                         lambda e: e.count('U'), lambda e: e.count('u')]
    
    for e in extensions_lambda:
        if output == '' and e(class_name) > 0:
            output = class_name + '.' + e(class_name).__str__()
        elif output != '' and e(class_name) > e(output):
            output = class_name + '.' + e(class_name).__str__()
    return output
