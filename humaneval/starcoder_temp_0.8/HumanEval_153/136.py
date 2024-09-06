
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
    # Your code here
    # cap is the number of uppercase letters
    # sm is the number of lowercase letters
    cap = 0
    sm = 0
    for char in class_name:
        if char.isupper():
            cap += 1
        elif char.islower():
            sm += 1
    # convert the strongest extension to its strength
    strength = cap - sm
    #print(class_name)
    #print(extensions)
    #print("strength is", strength)
    #print("cap is", cap)
    #print("sm is", sm)
    # initialize the strongest extension to be the class name
    strongest_extension = class_name
    # iterate through the extensions
    for extension in extensions:
        # convert the extension to its strength
        ext_cap = 0
        ext_sm = 0
        for char in extension:
            if char.isupper():
                ext_cap += 1
            elif char.islower():
                ext_sm += 1
        #print("ext_cap is", ext_cap)
        #print("ext_sm is", ext_sm)
        #print("ext_strength is", ext_cap - ext_sm)
        if ext_cap - ext_sm > strength:
            strength = ext_cap - ext_sm
            #print(extension, "is the strongest extension")
            strongest_extension = extension
    #print("strongest_extension is", strongest_extension)
    return class_name + "." + strongest_extension
