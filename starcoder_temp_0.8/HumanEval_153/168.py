
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
    #Initialize the strength of the strongest extension to zero.
    strongest_extension_strength = 0
    
    #Initialize the name of the strongest extension to be the first
    #extension in the list.
    strongest_extension_name = extensions[0]
    
    #Loop through the extensions:
    for extension in extensions:
        #Count the number of uppercase letters and the number of lowercase
        #letters in the extension's name.
        upper_count = 0
        lower_count = 0
        for letter in extension:
            if letter.isupper():
                upper_count += 1
            elif letter.islower():
                lower_count += 1
        
        #Calculate the strength of the extension.
        strength = upper_count - lower_count
        
        #Check whether the current extension is strongest than the strongest
        #extension found so far.
        if strength > strongest_extension_strength:
            strongest_extension_strength = strength
            strongest_extension_name = extension
    
    #Return the name of the strongest extension.
    return class_name + "." + strongest_extension_name
