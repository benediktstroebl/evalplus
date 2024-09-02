
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
    extensions.sort(key=lambda x: x.count('A') - x.count('s'), reverse=True)
    return class_name + '.' + extensions[0]

def GetClassFullName(className, packageName):
    """Given a class name and a package name, returns the full name of the class"""
    className = className.replace('.', '')
    for name in dir(packageName):
        if name.lower() == className.lower():
            return packageName.replace('.' + className, '').replace('.', '').split('.')[-1]
    return None

def GetClassExtensionNames(className, packageName):
    """Given a class name and a package name, returns a list of the extensions for the class"""
    packageName = GetClassFullName(packageName, packageName)
    if packageName is None:
        return []
    className = GetClassFullName(className, packageName)
    if className is None:
        return []
    extensions = className.replace('.', '').split('.')
    extensions.reverse()
    return extensions[:-1]

def GetStrongestExtension(class_name, extensions):
    """Given a class name and a list of extensions, returns the strongest extension"""
    return Strongest_Extension(class_name, extensions)

def GetStrongestExtensionNames(class_name, package_name):
    """Given a class name and a package name, returns a list of the strongest extensions for the class"""
    package_name = GetClassFullName(package_name, package_name)
    if package_name is None:
        return []
    class_name = GetClassFullName(class_name, package_name)
    if class_name is None:
        return []
    extensions = GetClassExtensionNames(class_name, package_name)
    return [GetStrongestExtension(name, extensions) for name in GetClassExtensionNames(class_name, package_name)]
