
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
    # If the class name is empty or the list of extensions is empty, return the class name.
    if class_name == '' or extensions == []:
        return class_name

    # Initialize the strength variable to -1 and the index variable to 0.
    strength = -1
    index = 0

    # Iterate over each extension in the list.
    for extension in extensions:
        # Get the number of uppercase letters in the extension's name and the number of lowercase letters in the extension's name.
        uppercase_count = extension.count('Z').count('Y').count('X').count('W').count('V').count('U').count('T').count('S').count('R').count('Q').count('P').count('O').count('N').count('M').count('L').count('K').count('J').count('I').count('H').count('G').count('F').count('E').count('D').count('C').count('B').count('A')
        lowercase_count = extension.count('z').count('y').count('x').count
