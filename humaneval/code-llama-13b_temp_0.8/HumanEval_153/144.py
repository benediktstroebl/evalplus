
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
    cap_num = 0
    cap_place = 0
    low_num = 0
    low_place = 0
    for i in range(len(extensions)):
        for x in extensions[i]:
            if x.isupper():
                cap_num += 1
            if x.islower():
                low_num += 1
    for i in range(len(extensions)):
        for x in extensions[i]:
            if x.isupper() and cap_place == 0:
                cap_place = cap_num
                cap_num = 0
            if x.isupper() and cap_place != 0:
                cap_num += 1
            if x.islower() and low_place == 0:
                low_place = low_num
                low_num = 0
            if x.islower() and low_place != 0:
                low_num += 1
    for i in range(len(extensions)):
        if cap_place == cap_num and low_place == low_num:
            return f'{class_name}.{extensions[i]}'
        
