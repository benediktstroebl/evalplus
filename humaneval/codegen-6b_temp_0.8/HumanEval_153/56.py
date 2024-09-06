
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
    # Replace this code with your own
    
    #This is a list of the letters in the extension names
    extension_letters = [x[0] for x in extensions]
    #this is a list of the extensions
    extensions_list = [x[1:] for x in extensions]
    
    sum_of_uppercase = 0
    sum_of_lowercase = 0
    for letter in extension_letters:
        if letter.isupper():
            sum_of_uppercase += 1
        elif letter.islower():
            sum_of_lowercase += 1
            
    #this is the strength of the extensions
    strength_of_extensions = sum_of_uppercase - sum_of_lowercase
    
    #lets find the strongest extension
    strongest_extension = extensions[0]
    
    for extension in extensions_list:
        current_strength = 0
        for letter in extension:
            if letter.isupper():
                current_strength += 1
            elif letter.islower():
                current_strength -= 1
                
        if current_strength > strength_of_extensions:
            strongest_extension = extension
        
    #now the name of the class
    class_name = class_name + '.' + strongest_extension
        
    return class_name
