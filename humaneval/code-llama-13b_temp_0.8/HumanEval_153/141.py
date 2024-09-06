
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
    strong_list = []
    for extension in extensions:
        #uppercase letters
        upper_count = 0
        #lowercase letters
        lower_count = 0
        #count uppercase and lowercase letters
        for char in extension:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
        #the number of uppercase letters - the number of lowercase letters
        strength = upper_count - lower_count
        #add the extension to the list with its strength
        strong_list.append([extension, strength])
    #sort the list by strength in descending order
    strong_list.sort(key=lambda x: x[1], reverse=True)
    #the strongest extension is the first element of the list
    strongest = strong_list[0][0]
    return class_name + '.' + strongest

