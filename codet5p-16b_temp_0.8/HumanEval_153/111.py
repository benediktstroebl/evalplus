
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

    pass # write your code here
    class_list = class_name.split('.')
    class_name = class_list[0]
    extensions = extensions[:]
    extensions.sort()
    for extension in extensions:
        extension_list = extension.split('.')
        extension_name = extension_list[0]
        count_upper = 0
        count_lower = 0
        for letter in extension_name:
            if letter.isupper():
                count_upper += 1
            else:
                count_lower += 1
        strength = count_upper - count_lower
        extension_string = extension_name + '.' + extension_list[1]
        extension_list[0] = extension_string
        extension_list[1] = strength
        extension = extension_list[0] + '.' + extension_list[1]
        extensions.remove(extension)
        extensions.insert(0, extension)
    strongest_extension = class_name + '.' + extensions[0]
    return strongest_extension
