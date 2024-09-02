
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
    
    result = None
    ext_idx = None
    for i, ext in enumerate(extensions):
        if not result:
            result = ext
            ext_idx = i
        else:
            tmp_strength = 0
            for j, l in enumerate(ext):
                if l.isupper():
                    tmp_strength += 1
                elif l.islower():
                    tmp_strength -= 1
            
            if tmp_strength > 0 and (not result.isupper() or tmp_strength > result.count('.')):
                result = ext
                ext_idx = i
            elif tmp_strength < 0 and (not result.islower() or tmp_strength < result.count('.')):
                result = ext
                ext_idx = i
    
    return ".".join([class_name, result])
    