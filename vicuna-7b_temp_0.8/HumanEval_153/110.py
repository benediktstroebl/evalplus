
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
    #Initialize a variable to keep track of the strongest extension
    strongest_extension = None
    #Initialize a variable to keep track of the strength of each extension
    extension_strength = {}
    #Iterate over the list of extensions
    for extension in extensions:
        #Calculate the strength of the extension
        strength = -1
        cap = 0
        sm = 0
        for letter in extension:
            if letter.upper() == letter:
                cap += 1
            else:
                sm += 1
        strength = cap - sm
        #If this is the first time we've seen an extension, or the strength is
        #higher, update the strongest extension and strength
        if strongest_extension is None or strength > extension_strength[strongest_extension]:
            strongest_extension = extension
            extension_strength[extension] = strength
    #If there are multiple extensions with the same strength, return the one
    #that comes first in the list
    return extension_strength.keys()[0] if extension_strength.keys() else None
