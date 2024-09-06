
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
    class_name = class_name
    class_name_list = []
    class_name_list.append(class_name)
    for i in extensions:
        extensions_list = list(i)
        extensions_list_lower = []
        extensions_list_upper = []
        for k in extensions_list:
            if k.isupper():
                extensions_list_upper.append(k)
            elif k.islower():
                extensions_list_lower.append(k)
        counter_upper = len(extensions_list_upper)
        counter_lower = len(extensions_list_lower)
        result = counter_upper - counter_lower
        if result > 0:
            class_name_list.append(i)
    class_name_list.sort()
    result_str = class_name + '.' + class_name_list[0]
    return result_str
