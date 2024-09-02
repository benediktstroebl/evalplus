
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
    # to index an element in a list you need to do [num-1] if it is zero indexed
    # the idea is to put the strength and the name in a list of lists
    # then sort the list by the strength
    # and take the first element [0]
    return_list = []
    for elem in extensions:
        strong = len([x for x in elem if x.isupper()]) - len([x for x in elem if x.islower()])
        return_list.append([strong,elem])
    return_list.sort(key = lambda x: x[0])
    return class_name + "." + return_list[-1][1]

