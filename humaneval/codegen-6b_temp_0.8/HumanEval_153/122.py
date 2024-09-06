
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
    class_name_and_extensions = [class_name] + extensions
    extensions = list(map(str.lower, extensions))
    class_name = str.lower(class_name)
    dic = dict(zip(range(len(class_name_and_extensions)), class_name_and_extensions))
    
    def comparator(key):
        char_index = ord(key) - ord('a')
        if dic[char_index].isupper():
            num = 1
        else:
            num = -1
        return num

    for i in range(len(class_name_and_extensions)):
        if i == 0:
            max_index = i
            max_value = comparator(dic[max_index][0])
        else:
            if comparator(dic[i][0]) > max_value:
                max_index = i
                max_value = comparator(dic[i][0])
    
    return class_name_and_extensions[max_index] + '.' + dic[max_index][:dic[max_index].find('.')]
