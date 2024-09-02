
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
    strongest = []
    #Given the class name, make a list of CAP and SM
    for extension in extensions:
        #Count the number of uppercase letters in the string
        CAP = 0
        for i in extension:
            if i == i.upper():
                CAP +=1
        #Count the number of lowercase letters in the string
        SM = 0
        for j in extension:
            if j == j.lower():
                SM +=1
        #The strength of the extension is as follows: the fraction CAP - SM
        strength = CAP - SM
        strongest.append((extension, strength))
    #Find the strongest extension and return a string in this format: ClassName.StrongestExtensionName.
    #If there are two or more extensions with the same strength, you should
    #choose the one that comes first in the list.
    strongest.sort(key=lambda x: x[1], reverse=True)
    return class_name + '.' + strongest[0][0]

