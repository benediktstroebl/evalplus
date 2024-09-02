
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
    def compare(x, y):
        x = x.lower()
        y = y.lower()
        return (x > y) - (x < y)
    extensions = set(extensions)
    stl = sorted(extensions, cmp=compare)
    for i in range(len(stl)):
        if stl[i].isupper():
            stl[i] = stl[i].lower()
        else:
            stl[i] = stl[i].upper()
    count = {}
    for e in stl:
        c = len(e) - count.get(e, 0)
        if c > 0:
            count[e] = c
    s = sorted(count.items(), cmp=lambda x,y: compare(x[0], y[0]))
    return '%s.%s'%(class_name, s[-1][0])
