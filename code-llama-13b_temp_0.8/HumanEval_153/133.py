
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
    import re
    upper = 0
    lower = 0
    class_str = class_name.lower()
    cap_count = 0
    lower_count = 0
    strong = 0
    strongest = []
    strong_name = ''
    for i in extensions:
        upper = 0
        lower = 0
        cap_count = 0
        lower_count = 0
        strong = 0
        if i.lower() == class_str:
            return class_name + '.' + i
        else:
            for j in i:
                if j.isupper():
                    upper += 1
                    cap_count += 1
                elif j.islower():
                    lower += 1
                    lower_count += 1
        strong = cap_count - lower_count
        strongest.append([i, strong])
    for i in strongest:
        if i[1] == strongest[0][1]:
            strong_name = i[0]
        else:
            pass
    return class_name + '.' + strong_name

