
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
    class_name_list = class_name.split(".")
    class_name_len = len(class_name_list)
    max_cap_minus_sm = -1
    max_cap_minus_sm_extension = ""
    for ext in extensions:
        ext_list = ext.split(".")
        cap_minus_sm = 0
        if ext_list[0:class_name_len] == class_name_list:
            cap_minus_sm = len(ext_list) - class_name_len - len(ext_list[class_name_len:])
        if cap_minus_sm > max_cap_minus_sm:
            max_cap_minus_sm = cap_minus_sm
            max_cap_minus_sm_extension = ext
    return class_name + "." + max_cap_minus_sm_extension

