
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
    dic = {}
    for i in range(len(extensions)):
        sum1 = 0
        sum2 = 0
        for j in extensions[i]:
            if j.isupper():
                sum1 = sum1 + 1
            if j.islower():
                sum2 = sum2 + 1
        if sum1 - sum2 in dic:
            dic[sum1 - sum2].append(extensions[i])
        else:
            dic[sum1 - sum2] = [extensions[i]]
    li = list(dic.keys())
    li.sort()
    return class_name + '.' + dic[li[-1]][0]

