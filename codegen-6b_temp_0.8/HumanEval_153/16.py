
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
    ext=[]
    for e in extensions:
        ext.append([e, 0])
    for i in range(len(ext)):
        for j in range(len(class_name)):
            if class_name[j]==ext[i][0][j]:
                ext[i][1]+=1
            elif class_name[j].isupper()==ext[i][0][j].isupper():
                ext[i][1]-=1
    max_value=0
    max_index=0
    for i in range(len(ext)):
        if max_value<ext[i][1]:
            max_value=ext[i][1]
            max_index=i
    return class_name+"."+ext[max_index][0]

    
