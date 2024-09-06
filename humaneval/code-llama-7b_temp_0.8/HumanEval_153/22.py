
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
    import string
    
    class_name = class_name + "."
    counter = 0
    extension_name = ""
    for ext in extensions:
        counter_cap = 0
        counter_sm = 0
        for c in ext:
            if c.isupper():
                counter_cap += 1
            if c.islower():
                counter_sm += 1
        if counter == 0:
            counter = -1*(counter_cap-counter_sm)
            extension_name = ext
        else:
            temp_counter = -1*(counter_cap-counter_sm)
            if temp_counter > counter:
                counter = temp_counter
                extension_name = ext
    return class_name + extension_name
