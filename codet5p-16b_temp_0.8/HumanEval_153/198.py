
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

    class_name = class_name.split('.')[0]
    extension_names = [ext.split('.')[1] for ext in extensions]
    cap_list = []
    sm_list = []
    for ext in extension_names:
        cap_list.append(len(ext))
        sm_list.append(len(ext.lower()))
    cap_num = sum(cap_list)
    sm_num = sum(sm_list)
    strength = cap_num - sm_num
    strong_ext = ""
    for ext in extension_names:
        if strength == max(cap_list) - min(sm_list):
            strong_ext = ext
            break
    return class_name + '.' + strong_ext
    
