
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
    class_name_list = list(class_name)
    index_class_name = [i for i, v in enumerate(class_name_list) if v.isupper()]
    str_class_name = "".join(class_name_list[i] for i in index_class_name)
    if not extensions:
        return class_name
    else:
        extension_list = []
        for i in extensions:
            extension_list.append(list(i))
        index_ext_list = []
        for i in extension_list:
            index_ext_list.append([i.index(v) for v in i if v.isupper()])
        # print(index_ext_list)
        index_ext_list_zip = list(zip(*index_ext_list))
        str_ext_list = []
        for i in index_ext_list_zip:
            str_ext_list.append("".join(extension_list[0][i] for i in i))
        # print(str_ext_list)
        return class_name + "." + extensions[str_ext_list.index(max(str_ext_list))]
