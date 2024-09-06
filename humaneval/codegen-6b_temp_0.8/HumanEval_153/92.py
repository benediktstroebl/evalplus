
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
    import string
    strength = 0
    for e in extensions:
        cap = 0
        l = []
        for letter in e:
            if letter in string.ascii_uppercase:
                cap += 1
                l.append(letter)
            elif letter in string.ascii_lowercase:
                l.append(letter)

        s = len(l) - cap

        if s > strength:
            strongest = e
            strength = s
    return class_name + "." + strongest

assert  Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == "my_class.AA"
assert Strongest_Extension("Issue", ['Issue', 'Brains', 'Backpack', 'Solved']) == "Issue.Brains"
assert Strongest_Extension("Other", ['Other', 'Esperance', 'SomeTool', 'MoreTool']) == "Other.Esperance"
assert Strongest_Extension("test", ['test', 'test1', 'test2']) == "test1.test2"
assert Strongest_Extension("test", ['test', 'test1', 'test2']) == "test2.test1"
assert Strongest_Extension("test", ['test', 'test1', 'test2']) == "test1.test2"

