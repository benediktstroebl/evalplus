
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
    if class_name=="":
        return ""
    if len(extensions)==0:
        return class_name
    if len(class_name)==0:
        return ""
    extensions_strength=[(len(x.upper())-len(x.lower())) for x in extensions]
    if extensions_strength==[]:
        return class_name
    #find the maximum strength in the extension list
    max_strength=max(extensions_strength)
    #find the extensions with max strength
    index=extensions_strength.index(max_strength)
    #return the strongest extension
    return class_name+"."+extensions[index]
