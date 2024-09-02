
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
    
    strength = 0
    
    for extension in extensions:
        
        upper = 0
        lower = 0
        
        for letter in extension:
            if letter.isupper():
                upper += 1
            elif letter.islower():
                lower += 1
        
        strength += upper - lower
        
    class_name_length = len(class_name)
        
    if strength == 0 or class_name_length - strength == 1:
        
        return "{}{.{}}".format(class_name, extensions[0])
    else:
        
        sorted_extensions = sorted(extensions, key=lambda extension: (len(extension), extension))
        
        return "{}{.{}}".format(class_name, sorted_extensions[0])