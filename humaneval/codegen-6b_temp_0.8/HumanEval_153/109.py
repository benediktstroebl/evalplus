
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
    ext_strength = [(s.count('A'), s.count('a'), s.count('E'), s.count('e'), s.count('G'), s.count('g'), s.count('I'), s.count('i'), s.count('N'), s.count('n'), s.count('U'), s.count('u'), s.count('F'), s.count('f'), s.count('S'), s.count('s'), s.count('V'), s.count('v')) for s in extensions]
    sorted_ext_strength = sorted(ext_strength, reverse=True)
    res = []
    for s in sorted_ext_strength:
        if s[0] != 0:
            res.append('a' * s[0] + 'e' * s[1] + 'g' * s[2] + 'i' * s[3] + 'n' * s[4] + 'u' * s[5] + 'f' * s[6] + 's' * s[7] + 'v' * s[8])
        else:
            res.append('e' * s[1] + 'g' * s[2] + 'i' * s[3] + 'n' * s[4] + 'u' * s[5] + 'f' * s[6] + 's' * s[7] + 'v' * s[8])
    return '{0}.{1}'.format(class_name, res[0])
