
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
    # to find the strength of the extension
    # find the number of uppercase letters in the extension's name
    cap = 0
    for i in extensions:
        for j in i:
            if j.isupper():
                cap += 1
    # find the number of lowercase letters in the extension's name
    sm = 0
    for i in extensions:
        for j in i:
            if j.islower():
                sm += 1
    # the strength of the extension is given by the fraction CAP - SM. 
    # we will use the absolute value since it may be negative
    strength = abs(cap - sm)
    # find the strongest extension
    # if there are two or more extensions with the same strength, you should
    # choose the one that comes first in the list.
    result = 0
    for i in range(len(extensions)):
        if strength == 0:
            break
        # find the number of uppercase letters in the extension's name
        cap = 0
        for j in extensions[i]:
            if j.isupper():
                cap += 1
        # find the number of lowercase letters in the extension's name
        sm = 0
        for j in extensions[i]:
            if j.islower():
                sm += 1
        # the strength of the extension is given by the fraction CAP - SM. 
        # we will use the absolute value since it may be negative
        new_strength = abs(cap - sm)
        if strength == new_strength:
            # if the strength is the same, we will find the first one
            # in the list
            if result == 0:
                result = i
            else:
                if i < result:
                    result = i
        elif new_strength < strength:
            strength = new_strength
            result = i
    # now we have the index of the strongest extension
    # we need to return the string in this format: ClassName.StrongestExtensionName
    return class_name + '.' + extensions[result]

