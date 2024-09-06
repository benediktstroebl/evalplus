
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
    from collections import Counter
    extensions = [ext.lower() for ext in extensions]
    counter = Counter(extensions)
    sorted_counter = sorted(counter.items(), key=lambda x:x[1])
    sorted_counter = sorted(sorted_counter, key=lambda x:x[1], reverse=True)
    strongest_extension = None
    for item in sorted_counter:
        if item[1] > 1:
            continue
        code = ''.join([letter for letter in item[0] if letter.isupper()])
        code1 = ''.join([letter for letter in item[0] if letter.islower()])
        if strong_extension is None or code > code1:
            strongest_extension = item[0]
            break
    return "{0}.{1}".format(class_name, strongest_extension)
