
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
    if not extensions:
        return class_name
    comparison_function = lambda x,y: -1 if x<y else 1 if x>y else 0
    highest_strength = max(enumerate(extensions), key=lambda x: comparison_function(len(x[1]), len(class_name)))

    return "{}.{}".format(class_name, highest_strength[1])


my_string = "my_class"
my_list = ['AA', 'BE', 'CC']
my_string2 = "my_class_name"
my_list2 = ['AA', 'BE', 'CC', 'E']
my_string3 = "my_class_name_name"
my_list3 = ['AA', 'BE', 'CC']
