
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

    from collections import defaultdict
    from itertools import chain

    # Get the strength of each extension
    # strength = defaultdict(int)
    # for extension in extensions:
    #     strength[extension] = (sum(c.isupper() for c in extension) -
    #                             sum(c.islower() for c in extension))

    strength = {ext: (sum(c.isupper() for c in ext) -
                    sum(c.islower() for c in ext)) for ext in extensions}

    # Get the maximum strength
    max_strength = max(strength.values())

    # Get the extension with the maximum strength
    max_strength_ext = list(filter(lambda x: strength[x] == max_strength, strength))

    # If there is no extension with the maximum strength
    if not max_strength_ext:
        return class_name

    # Return the extension with the maximum strength
    return class_name + '.' + max_strength_ext[0]

