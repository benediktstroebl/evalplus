
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
    # Write your code here
    if extensions == []:
        return class_name
    elif len(extensions) == 1:
        return class_name + "." + extensions[0]
    elif len(extensions) > 1:
        for i in range(len(extensions)):
            # print("CAP: " + str(len([c for c in extensions[i] if c.isupper()])) + 
            #       " SM: " + str(len([c for c in extensions[i] if c.islower()])))
            # print("STR: " + str(len([c for c in extensions[i] if c.isupper()]) - 
            #        len([c for c in extensions[i] if c.islower()])))
            if i == 0:
                CAP = len([c for c in extensions[i] if c.isupper()])
                SM = len([c for c in extensions[i] if c.islower()])
                STRENGTH = CAP - SM
            elif len([c for c in extensions[i] if c.
