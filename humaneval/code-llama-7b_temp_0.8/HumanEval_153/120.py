
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
    # Introduce a variable to keep track of the strength
    Strength = 0
    # Introduce a variable to hold the Extension
    StrongestExtension = ""
    # Loop over the extensions
    for i in extensions:
        # Calculate the Strength
        CAP = 0
        SM = 0
        # Find the number of uppercase letters in the extension
        for j in i:
            if j.isupper():
                CAP += 1
        # Find the number of lowercase letters in the extension
        for j in i:
            if j.islower():
                SM += 1
        # If the Strength is less than the CAP - SM
        if Strength < (CAP - SM):
            # Set Strength to CAP - SM
            Strength = (CAP - SM)
            # Set StrongestExtension to i
            StrongestExtension = i
    # Return class_name and StrongestExtension as a string
    return class_name + '.' + StrongestExtension

