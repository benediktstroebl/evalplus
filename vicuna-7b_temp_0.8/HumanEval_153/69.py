
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
    # This is a recursive approach
    extension_list = sorted(extensions, key=lambda x: x.lower().count('a'))
    extension_list = [''.join(filter(lambda x: x.isalpha(), x)) for x in extension_list]
    extension_name = ''.join(filter(lambda x: x.isalpha(), ' '.join(extension_list)))
    class_name = class_name.lower()
    extension_name = extension_name.lower()
    extension_name = extension_name.replace('.', '')
    if class_name == extension_name:
        return class_name + '.' + extension_name
    else:
        for i in range(len(extension_list) - 1):
            extension_strength = class_name.count(extension_list[i]) - class_name.count(extension_list[i + 1])
            if extension_strength > 0:
                return class_name + '.' + extension_list[i] + '.' + extension_name
        return class_name + '.' + extension_list[-1] + '.' + extension_name
