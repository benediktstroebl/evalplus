
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
    class_name_list_upper = list(class_name.upper())
    class_name_list_lower = list(class_name.lower())
    class_name_upper = ''.join(class_name_list_upper)
    class_name_lower = ''.join(class_name_list_lower)
    class_name_upper_len = len(class_name_upper)
    class_name_lower_len = len(class_name_lower)
    strongest_extension = ""
    strongest_extension_numerator = 0
    strongest_extension_denominator = 0
    
    for extension in extensions:
        extension_list = list(extension)
        extension_list_upper = list(extension.upper())
        extension_list_lower = list(extension.lower())
        extension_upper = ''.join(extension_list_upper)
        extension_lower = ''.join(extension_list_lower)
        extension_upper_len = len(extension_upper)
        extension_lower_len = len(extension_lower)
        extension_numerator = extension_upper_len - extension_lower_len
        extension_denominator = extension_lower_len - class_name_lower_len
        if extension_numerator > strongest_extension_numerator:
            strongest_extension = ''.join(class_name_list) + '.' + ''.join(extension_list)
            strongest_extension_numerator = extension_numerator
            strongest_extension_denominator = extension_denominator
        elif extension_numerator == strongest_extension_numerator:
            if extension_denominator < strongest_extension_denominator:
                strongest_extension = ''.join(class_name_list) + '.' + ''.join(extension_list)
                strongest_extension_numerator = extension_numerator
                strongest_extension_denominator = extension_denominator
    return strongest_extension

