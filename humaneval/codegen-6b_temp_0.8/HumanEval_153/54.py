
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
    strength = 0
    chars = []
    for extension in extensions:
        for char in extension:
            if char.isupper():
                strength += 1
            else:
                strength -= 1
        chars.append([strength, extension])
        strength = 0
    #print(chars)
    strongest = sorted(chars, key = lambda x:x[0])[-1][1]
    return '{}.{}'.format(class_name, strongest)
    
assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
assert Strongest_Extension('my_class', ['acCC', 'BBb', 'Eee']) == 'my_class.acCC'
assert Strongest_Extension('AA', ['aaa', 'AbB']) == 'AA.aaa'
assert Strongest_Extension("myLife", ["myLife", "mymoLifE"]) == "myLife.mymoLifE"
assert Strongest_Extension("myLife", ["mymoLifE", "myLife"]) == "myLife.mymoLifE"