
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
    strongest_extension = ''
    extension_strength = 0
    # go through the extensions
    for extension in extensions:
        # get the strength of this extension
        extension_strength = extension.count('A') - extension.count('a')
        # if this extension is stronger than the current strongest extension
        if extension_strength > extension_strength:
            # update the strongest extension
            strongest_extension = extension
        # if this extension is equally strong
        elif extension_strength == extension_strength:
            # check if the current extension is earlier in the list
            if extension < strongest_extension:
                # update the strongest extension
                strongest_extension = extension
    # return the class name and the strongest extension
    return f'{class_name}.{strongest_extension}'

