
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
    if len(extensions) == 0:
        return class_name
    
    ext_name, strength = extensions[0], 0
    for ext in extensions[1:]:
        if len(ext) > len(ext_name):
            ext_name, strength = ext, 0
        else:
            ext_name, strength = ext, -1
    
    return '%s.%s' % (class_name, ext_name)

def Strongest_Extension_Recursive(class_name, extensions, level=0):
    """This function is used to find the strongest extension for a class.
    It is recursive and it will follow the inheritance hierarchy,
    if a class is an extension of another class, the strongest 
    extension will be the one that is directly in the hierarchy
    before the class.
    It uses the Strongest_Extension function.
    """
    if len(extensions) == 0:
        return class_name
    
    ext_name, strength = extensions[0], 0
    for ext in extensions[1:]:
        if level == len(ext) - 1:
            # if the extension is in the hierarchy before the class,
            # it is the strongest extension
            return Strongest_Extension(class_name, ext)
        else:
            # otherwise, continue looking in the hierarchy
            if level > 0:
                # if the extension is an extension of an extension
                # of the class, the strongest extension will be
                # the one that is directly in the hierarchy before the class
                return Strongest_Extension_Recursive(class_name, ext, level-1)
            else:
                # otherwise, if the extension is an extension of the class,
                # the strongest extension will be the one that is directly
                # before the class in the hierarchy
                return Strongest_Extension(class_name, ext)
    
    return class_name
