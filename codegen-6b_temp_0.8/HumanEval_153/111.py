
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
    ext_lengths = [len(extension) for extension in extensions]
    
    max_strength = max(ext_lengths)
    max_strength_idx = ext_lengths.index(max_strength)
    
    max_strength_extension = extensions[max_strength_idx]
    
    letter_counts = [0] * 26
    
    for extension in extensions:
        for letter in extension:
            x = ord(letter) - 97
            letter_counts[x] += 1
    
    max_count_idx = letter_counts.index(max(letter_counts))
    max_count = letter_counts[max_count_idx]
    
    if max_strength == max_count:
        return class_name + "." + max_strength_extension
    else:
        return class_name + "." + max_count_extension
