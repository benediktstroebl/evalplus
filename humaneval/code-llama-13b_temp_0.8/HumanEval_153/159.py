
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
    new_extensions = []
    for x in extensions:
        capital = 0
        small = 0
        for y in x:
            if y.isupper():
                capital += 1
            else:
                small += 1
        new_extensions.append((x, capital - small))
    max_capital = max(new_extensions, key=lambda x: x[1])[1]
    max_extensions = [i for i in new_extensions if i[1] == max_capital]
    max_extensions = sorted(max_extensions, key=lambda x: x[0])
    max_extension = max_extensions[0][0]
    return class_name + '.' + max_extension
