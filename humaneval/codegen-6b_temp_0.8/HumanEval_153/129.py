
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
    
    """
    >>> Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])
    'Slices.SErviNGSliCes'
    
    """
    
    # first we create a dictionary of extensions' loops using their extension name
    extension_list = {}
    for extension in extensions:
        extension_list[extension] = len(extension) - extension.count(".")
        
    # we compute all extension's loops and store in a list
    loop_list = []
    for extension in extension_list:
        loop = 0
        for extension_part in extension.split("."):
            loop += (ord(extension_part[0]) - ord("A"))
            loop += (ord(extension_part[-1]) - ord("a"))
        loop_list.append(loop)
    
    # we create a dictionary of extension loop's index and extension names
    dct = {}
    i = 0
    for extension in extension_list:
        dct[loop_list[i]] = extension
        i += 1
    
    # then we sort the dictionary by loop
    sort = sorted(dct.keys(), reverse=True)
    
    # we just need the highest loop
    return dct[sort[0]] + "." + dct[sort[0]] + ".StrongestExtension"
    
    