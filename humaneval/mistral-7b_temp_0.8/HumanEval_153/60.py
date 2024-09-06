
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
    if class_name == None or extensions == None:
        return None
    list1 = []
    for i in range(len(extensions)):
        tmp = 0
        for j in extensions[i]:
            if j.isupper():
                tmp += 1
            else:
                tmp -= 1
        list1.append((extensions[i], tmp))
    max = list1[0][1]
    max_name = list1[0][0]
    for i in range(len(list1)):
        if list1[i][1] > max:
            max = list1[i][1]
            max_name = list1[i][0]
    return class_name + '.' + max_name


