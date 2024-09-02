
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
    #Split the name of the class and the extension
    name, extension = class_name.split(".")

    #Find the strength of each extension
    extension_strength = [len(x) - len(x.lower()) for x in extensions]
    
    #Find the strongest extension
    strongest_index = extension_strength.index(max(extension_strength))
    strongest_extension = extensions[strongest_index]
    
    #Return the string
    return "{0}.{1}".format(name, strongest_extension)
    
    
tests = ["my_class.EE", "my_class.E", "my_class.BE", "Slices.SErviNGSliC",
         "my_class.EE", "my_class.E", "my_class.BE", "Slices.SErviNGSliC",
         "my_class.EE", "my_class.E", "my_class.BE", "Slices.SErviNGSliC"]

for test in tests:
    print Strongest_Extension(test, ['EE', 'E', 'BE'])
    print Strongest_Extension(test, ['EE', 'E', 'BE', 'AE'])
    print Strongest_Extension(test, ['EE', 'E', 'BE', 'AE', 'CA'])
    print Strongest_Extension('my_class.EE', ['EE', 'E', 'BE', 'AE', 'CA'])



