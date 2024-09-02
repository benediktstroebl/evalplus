
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
    # This is a list of tuples, where each tuple contains the class name and its extensions
    class_and_exts = [("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']),
                       ("Other", ['Unknown', 'UnheardOf', 'Unknown'])
                       ]
    
    #sort by the number of uppercase letters in the extension name
    sorted_class_and_exts = sorted(class_and_exts, key=lambda x: len(x[1].upper()))
    
    # find the first extension in the list that satisfies the condition
    for cls, exts in sorted_class_and_exts:
        if len(exts) == 1 and exts[0].lower() == class_name.lower():
            return cls + "." + exts[0]
    
    return None