
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
    #Write your code here
    #raise NotImplementedError
    if len(extensions) == 0:
        return class_name
    else:
        max_strength = 0
        max_extension_name = ""
        for extension in extensions:
            if extension[0].isupper():
                uppercase = 1
            else:
                uppercase = 0
            if extension[0].islower():
                lowercase = 1
            else:
                lowercase = 0
            strength = uppercase - lowercase
            if strength > max_strength:
                max_extension_name = extension
                max_strength = strength
        return class_name + '.' + max_extension_name
