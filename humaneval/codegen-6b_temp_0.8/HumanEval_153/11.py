
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
    list_strength = []
    for extension in extensions:
        UPPERCASE = 0
        LOWERCASE = 0
        for char in extension:
            if char.isupper():
                UPPERCASE += 1
            elif char.islower():
                LOWERCASE += 1
        couple = (UPPERCASE - LOWERCASE, extension)
        list_strength.append(couple)
    max_strength = max(list_strength, key=lambda x: x[0])[0]
    list_class = []
    for i in list_strength:
        if i[0] == max_strength:
            list_class.append(i[1])
    return "{}.{}".format(class_name, list_class[0])

