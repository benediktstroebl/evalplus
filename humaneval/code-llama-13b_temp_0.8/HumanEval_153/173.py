
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
    # your code here
    #the base case
    if extensions == []:
        return class_name
    
    #the base case
    if extensions == [class_name]:
        return class_name + '.' + class_name
    
    #the recursive step
    else:
        
        #start with the first element of the list
        index = 0
        current_extension = extensions[index]
        
        #get the fraction
        cap = sum(1 for letter in current_extension if letter.isupper())
        sm = sum(1 for letter in current_extension if letter.islower())
        strength = cap - sm
        
        #check if the other extensions are stronger than the current_extension
        for extension in extensions[1:]:
            
            #get the fraction
            cap = sum(1 for letter in extension if letter.isupper())
            sm = sum(1 for letter in extension if letter.islower())
            next_extension_strength = cap - sm
            
            #check if the next extension is stronger than the current_extension
            if next_extension_strength > strength:
                
                #change current_extension to be the next extension
                current_extension = extension
                
                #change strength to be the strength of next extension
                strength = next_extension_strength
        
        #return the class name and the strongest extension
        return class_name + '.' + current_extension
