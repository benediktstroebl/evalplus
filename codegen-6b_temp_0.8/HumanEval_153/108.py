
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
    class_name = class_name.lower()
    ext_strength = []
    for x in extensions:
        x = x.lower()
        if x.count('z') == len(x):
            x = x.replace('z','26')
        x = x.replace('j','11')
        x = x.replace('b','2')
        x = x.replace('a', '1')
        x = x.replace('c', '13')
        x = x.replace('t', '11')
        strength = x.count('26') - x.count('11') + x.count('2') - x.count('1') + x.count('13') - x.count('11')
        ext_strength.append(strength)
    return '%s.%s'%(class_name,extensions[ext_strength.index(max(ext_strength))])

