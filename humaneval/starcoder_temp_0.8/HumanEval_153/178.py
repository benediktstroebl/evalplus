
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

    import re
    # regular expression to find upper and lower case letters
    pat = re.compile('[A-Z]|[a-z]')
    # list to hold names of extensions
    ext = []
    # create a list of extensions
    for i in range(len(extensions)):
        # store the extension name into ext
        ext.append(extensions[i])
        # get upper and lower case letters in the extension
        p = pat.findall(extensions[i])
        # compute strength of the extension
        s = (len(p) - sum(1 for letter in p if letter.isupper()))
        # add strength to a list
        strength = [extensions[i], s]
        # if strength list is empty
        if i == 0:
            # add list to strength list
            s_list = [strength]
        # if strength list has elements
        else:
            # check for the strength of the extension with minimum strength
            # if strength of the extension is less than the strength of the first element
            if s < s_list[0][1]:
                # append the strength of the extension to the list
                s_list.append(strength)
            # if strength of the extension is greater than or equal to
            # the strength of the first element
            else:
                # insert the extension into the first position of the strength list
                s_list.insert(0, strength)
    # the first element of the list will have the extension with minimum strength
    ext_name = s_list[0][0]
    # return the class name and the name of the extension
    return (class_name + '.' + ext_name)
