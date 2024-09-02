
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
    strongest_extension = extensions[0]
    strongest_extension_cap = strongest_extension.count(str.upper)
    strongest_extension_sm = strongest_extension.count(str.lower)
    strongest_extension_strength = strongest_extension_cap - strongest_extension_sm
    print(strongest_extension_strength)
    for extension in extensions[1:]:
        extension_cap = extension.count(str.upper)
        extension_sm = extension.count(str.lower)
        extension_strength = extension_cap - extension_sm
        print(extension_strength)
        if extension_strength > strongest_extension_strength:
            strongest_extension = extension
            strongest_extension_cap = extension_cap
            strongest_extension_sm = extension_sm
            strongest_extension_strength = extension_strength
            print(strongest_extension_strength)
        if extension_strength == strongest_extension_strength:
            if extension < strongest_extension:
                strongest_extension = extension
                strongest_extension_cap = extension_cap
                strongest_extension_sm = extension_sm
                strongest_extension_strength = extension_strength
                print(strongest_extension_strength)
    return "{}.{}".format(class_name, strongest_extension)

