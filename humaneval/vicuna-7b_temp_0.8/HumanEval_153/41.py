
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
    # Find the longest extension name
    max_length = 0
    max_strength = 0
    for ext in extensions:
        length = len(ext)
        strength = length - len(ext.lower())
        if strength > max_strength:
            max_strength = strength
            max_length = length
    max_strength_ext = ''.join(ext[i:].lower() for i in range(max_length))
    return class_name + '.' + max_strength_ext

def Generate_Test_Case(test_case):
    """Given a string test case, generate a test function
    """
    func_name = Strongest_Extension(test_case, [])
    return lambda: assert test_case == func_name, "The generated function does not match the test case."
def Generate_Test_Cases(className):
    """Generate a test case for each possible string in the given class
    """
    possible_strings = [word.lower() for word in open("possible_strings.txt").read().splitlines()]
    test_cases = [Generate_Test_Case(string) for string in possible_strings]
    return test_cases
def run_test_cases(test_cases):
    """Run each test case in the list
    """
    for test_case in test_cases:
        run(test_case())
