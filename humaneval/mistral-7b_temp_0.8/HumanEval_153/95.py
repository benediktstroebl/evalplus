
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
    # all lowercase, because I want to make sure, that the uppercase letters have a higher priority
    lower_case_extensions = []
    for extension in extensions:
        lower_case_extension = ""
        for letter in extension:
            lower_case_extension += letter.lower()
        lower_case_extensions.append(lower_case_extension)

    # all uppercase, because I want to make sure, that the uppercase letters have a higher priority
    upper_case_extensions = []
    for extension in extensions:
        upper_case_extension = ""
        for letter in extension:
            upper_case_extension += letter.upper()
        upper_case_extensions.append(upper_case_extension)

    extensions.sort(key=lambda x: x.lower())
    # we can add the extensions in the way we want, the extensions will be sorted by alphabetical order

    extension_with_highest_strength = 0
    for i, extension in enumerate(extensions):
        if i == 0
