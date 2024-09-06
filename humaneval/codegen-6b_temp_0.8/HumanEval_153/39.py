
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
    
    strongest_extension_name = []
    strongest_extension_name_strength = 0
    
    for extension in extensions:
        if extension != class_name:
            extension_uppercase = 0
            extension_lowercase = 0

            for letter in extension:
                if letter.isupper():
                    extension_uppercase += 1
                if letter.islower():
                    extension_lowercase += 1

            if extension_uppercase == 0 or extension_lowercase == 0:
                print "Invalid extension. Delete extension."
                continue

            extension_strength = float("%.2f" % ((extension_uppercase - extension_lowercase) / 2))
            if extension_strength > strongest_extension_name_strength:
                strongest_extension_name_strength = extension_strength
                strongest_extension_name = extension

    return class_name + "." + strongest_extension_name

