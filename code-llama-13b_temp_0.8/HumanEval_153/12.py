
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
    letter_counts = {}
    letter_counts_list = []
    for i in extensions:
        letter_counts[i] = [i.count(x) for x in i if x.isupper()]
        letter_counts[i].extend([i.count(x) for x in i if x.islower()])
        letter_counts_list.append(letter_counts[i][0] - letter_counts[i][1])
    
    strongest_extension = extensions[letter_counts_list.index(max(letter_counts_list))]
    return class_name + "." + strongest_extension

