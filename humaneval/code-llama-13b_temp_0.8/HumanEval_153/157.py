
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
    # This function is set up for you, simply fill in your code at the bottom
    # and return the answer. 
    # The function is set up as: Strongest_Extension(class_name, extensions)
    # Your code should return a string in this format: "ClassName.ExtensionName"
    # for example: "MyClass.MyExtension"

    strongest = 0
    strongest_name = ""
    for ext in extensions:
        # Your code here
    # The above code is set up as an example for you. 
    # You can modify it as you wish, or delete it altogether.
    # The function is set up as: Strongest_Extension(class_name, extensions)
    # Your code should return a string in this format: "ClassName.ExtensionName"
    # for example: "MyClass.MyExtension"
        cap_count = 0
        low_count = 0
        for char in ext:
            if char.isupper():
                cap_count += 1
            if char.islower():
                low_count += 1
        if (cap_count - low_count) > strongest:
            strongest = cap_count - low_count
            strongest_name = ext
    return class_name + "." + strongest_name
