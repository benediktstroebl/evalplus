
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
    class_name_up = class_name.upper()
    class_name_lo = class_name.lower()
    
    class_name_up_num = len(class_name_up)
    class_name_lo_num = len(class_name_lo)
    
    strongest_extension = []
    for extension in extensions:
        extension_up = extension.upper()
        extension_lo = extension.lower()
        extension_up_num = len(extension_up)
        extension_lo_num = len(extension_lo)
        ratio = extension_up_num - extension_lo_num
        strongest_extension.append((ratio, extension))
    sorted_extensions = sorted(strongest_extension)
    selected = sorted_extensions[0]
    result = f'{class_name}.{selected[1]}'
    return result

