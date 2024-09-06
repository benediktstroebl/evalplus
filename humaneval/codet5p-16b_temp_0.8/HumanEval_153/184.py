
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

    assert isinstance(class_name, str), "class_name should be a string"
    assert isinstance(extensions, list), "extensions should be a list"
    assert len(class_name) > 0, "class_name should be a non empty string"
    assert len(extensions) > 0, "extensions should be a non empty list"
    for i in extensions:
        assert isinstance(i, str), "all elements of extensions should be strings"
        assert len(i) > 0, "all elements of extensions should be non empty strings"
    cap = 0
    sm = 0
    s = []
    for i in class_name:
        if i.isupper():
            cap += 1
        else:
            sm += 1
    for j in extensions:
        cap_new = 0
        sm_new = 0
        for i in j:
            if i.isupper():
                cap_new += 1
            else:
                sm_new += 1
        s.append(round((cap_new - sm_new),1))
    s_max = max(
