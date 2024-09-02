
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
    class_name = class_name.split(".")[-1]
    all_classes = []
    for name in class_name.split("."):
        all_classes.append(name)
    all_classes.append(class_name)
    for name in extensions:
        for i in range(len(all_classes)):
            if all_classes[i] == name:
                all_classes.remove(name)
    max_strength = 0
    for i in range(len(all_classes)):
        for j in range(len(all_classes)):
            if i != j and all_classes[i].isalpha() and all_classes[j].isalpha():
                strength = len(all_classes[i].lower()) - len(all_classes[j].lower())
                if strength > max_strength:
                    max_strength = strength
    return class_name + "." + max_strength