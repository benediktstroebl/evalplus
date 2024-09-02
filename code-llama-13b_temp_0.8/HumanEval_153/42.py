
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
    class_name_up=class_name.upper()
    class_name_low=class_name.lower()
    class_name_up_len=len(class_name_up)
    class_name_low_len=len(class_name_low)
    class_name_strength=class_name_up_len-class_name_low_len
    strongest_extension=''
    strongest_extension_strength=0
    for extension in extensions:
        extension_up=extension.upper()
        extension_low=extension.lower()
        extension_up_len=len(extension_up)
        extension_low_len=len(extension_low)
        extension_strength=extension_up_len-extension_low_len
        if extension_strength>class_name_strength:
            strongest_extension=extension
            strongest_extension_strength=extension_strength
            class_name_strength=extension_strength
        elif extension_strength==class_name_strength and extension_strength>strongest_extension_strength:
            strongest_extension=extension
            strongest_extension_strength=extension_strength
    return class_name+'.'+strongest_extension

