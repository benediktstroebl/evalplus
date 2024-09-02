
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
    # Get the class name and extensions
    className = class_name
    extensions = list(extensions)
    
    # Get the full name of the class
    fullName = className + "." + "." + "." + extensions[0]
    
    # Get the capitalized and lowercased name of the class
    capitalizedName = className.upper()
    lowercaseName = className.lower()
    
    # Create a list of tuples, each tuple contains the extension name, the number of uppercase letters and the number of lowercase letters
    extensionInfo = [(extensions[i], len(capitalizedName) - len(lowercaseName[i]), len(lowercaseName[i])) for i in range(len(extensions))]
    
    # Find the strongest extension by sorting the tuples based on the strength
    extensionInfo = sorted(extensionInfo, key=lambda x: x[1] - x[2])
    
    # Find the index of the strongest extension in the extensions list
    idx = extensionInfo.index(extensionInfo.pop())
    
    # Create the full name of the class by concatenating the capitalized and lowercased name of the class and the strongest extension
    return fullName.format(idx=idx)
