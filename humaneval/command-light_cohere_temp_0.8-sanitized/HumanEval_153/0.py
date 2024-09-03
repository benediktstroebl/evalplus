def Strongest_Extension(class_name, extensions):
    """
    Extensions are to be used to load additional classes to the class.
    The strength of the extension is as follows: Let CAP be the number of the 
    uppercase letters in the extension's name, and let SM be the number of 
    lowercase letters in the extension's name, the strength is given by the fraction 
    CAP - SM.
    
    You strength of extensions should be compared to the class name to find the
    strongest one.

    Returns the string that contains the name of the strongest extension.
    """
    longest_extension = ''
    for extension in extensions:
        if Strongest_Extension(class_name, [CAP, SM]) == extension:
            longest_extension = extension
    return longest_extension
class_name = 'MyClass'
extensions = ['AA', 'Be', 'CC', 'DAS']