
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
    c_name= class_name
    l= extensions
    num_caps=0
    num_lows=0
    max_index= 0
    max_num= 0
    for i in l:
        for x in i:
            if x.isupper():
                num_caps+=1
            elif x.islower():
                num_lows+=1
    for j in range(len(l)):
        if num_caps - num_lows < max_num:
            break
        num_caps=0
        num_lows=0
        for x in l[j]:
            if x.isupper():
                num_caps+=1
            elif x.islower():
                num_lows+=1
        if num_caps - num_lows > max_num:
            max_index= j
            max_num= num_caps - num_lows
    return c_name+"."+l[max_index]
    
