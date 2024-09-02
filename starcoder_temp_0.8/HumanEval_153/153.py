
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
    strength = {}
    for item in extensions:
        count_upper = item.upper().count('A') + item.upper().count('B') + item.upper().count('C') + item.upper().count('D') + item.upper().count('E') + item.upper().count('F') + item.upper().count('G') + item.upper().count('H') + item.upper().count('I') + item.upper().count('J') + item.upper().count('K') + item.upper().count('L') + item.upper().count('M') + item.upper().count('N') + item.upper().count('O') + item.upper().count('P') + item.upper().count('Q') + item.upper().count('R') + item.upper().count('S') + item.upper().count('T') + item.upper().count('U') + item.upper().count('V') + item.upper().count('W') + item.upper().count('X') + item.upper().count('Y') + item.upper().count('Z')
        count_lower = item.lower().count('a') + item.lower().count('b') + item.lower().count('c') + item.lower().count('d') + item.lower().count('e') + item.lower().count('f') + item.lower().count('g') + item.lower().count('h') + item.lower().count('i') + item.lower().count('j') + item.lower().count('k') + item.lower().count('l') + item.lower().count('m') + item.lower().count('n') + item.lower().count('o') + item.lower().count('p') + item.lower().count('q') + item.lower().count('r') + item.lower().count('s') + item.lower().count('t') + item.lower().count('u') + item.lower().count('v') + item.lower().count('w') + item.lower().count('x') + item.lower().count('y') + item.lower().count('z')
        strength[item] = count_upper - count_lower
    return class_name + '.' + sorted(strength, key
