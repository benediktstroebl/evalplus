
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
    def compare(s1, s2):
        s1_caps = s1.upper()
        s1_lowers = s1.lower()
        s2_caps = s2.upper()
        s2_lowers = s2.lower()
        cap_diff = abs(len(s1_caps) - len(s2_caps))
        lower_diff = abs(len(s1_lowers) - len(s2_lowers))
        return cap_diff - lower_diff

    strengths = {}
    for e in extensions:
        strengths[e] = compare(class_name, e)
    sorted_strengths = sorted(strengths, key=lambda s: strengths[s])
    return f'{class_name}.{sorted_strengths[0]}'
