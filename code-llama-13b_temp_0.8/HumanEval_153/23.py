
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
    strong_list = []
    strong_index = 0
    for i in range(len(extensions)):
        caps = 0
        lowers = 0
        for c in extensions[i]:
            if c.isupper():
                caps += 1
            if c.islower():
                lowers += 1
        strength = caps - lowers
        strong_list.append(strength)
    for i in range(len(strong_list)):
        if strong_list[i] > strong_list[strong_index]:
            strong_index = i
    return class_name + "." + extensions[strong_index]

