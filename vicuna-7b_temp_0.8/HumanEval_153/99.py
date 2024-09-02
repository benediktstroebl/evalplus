
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
    # This is the function that will calculate the strength
    def calculate_strength(extension):
        # This function will take the extension as an argument
        # It will check if the extension is a class, and if it is, it will return the number of uppercase letters in the class name
        # minus the number of lowercase letters, ignoring the first letter (which is always uppercase)
        def check_extension(extension):
            # This function will check if the extension is a class
            if '.' not in extension:
                return 0
            # It will check if the extension is a class
            className, extension = extension.split('.')
            className = className.title()
            extension = extension.lower()
            return len(className.split()) - len(extension.split())
        # This function will take an extension and return its strength
        return check_extension(extension)
    # This function will find the strongest extension
    def find_strongest(extensions):
        strengths = []
        for extension in extensions:
            strength = calculate_strength(extension)
            strengths.append(str(extension) + '.' + str(strength))
        # This is the part of the function that finds the strongest extension
        # The strongest extension is the one that has the highest strength
        # We can use the Counter class from the collections module to get the strength of each extension
        max_strength = max(strengths, key=strengths.get, 0)
        # This line finds the strongest extension
        return '.'.join(max_strength.split())
    return find_strongest(extensions)
