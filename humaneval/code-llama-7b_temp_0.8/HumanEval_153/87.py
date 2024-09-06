
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
    class_name = class_name
    extensions = extensions
    # your code here

    # initiate the result value, the strength
    strength = 0

    # initiate the max strength
    max_strength = -100

    # initiate the result value, the strongest extension name
    strongest_extension_name = ""

    # loop through the list
    for extension in extensions:
        # get the current strength by calculate the difference between uppercase and lowercase letters in the extension name
        cur_strength = (extension.upper().count("A") - extension.lower().count("a"))
        # if the current strength is higher than max strength
        if cur_strength > max_strength:
            # update the max strength
            max_strength = cur_strength
            # update the strongest extension name
            strongest_extension_name = extension

    # return the result
    return "{}.{}".format(class_name, strongest_extension_name)
