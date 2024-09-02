
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
    # The list might be empty. In that case just return the class name.
    if not extensions:
        return class_name
    ext_name = extensions[0]
    # Find the index of the first uppercase letter of the extension's name.
    # Example: 'Be' returns 1.
    first_upper = ext_name.index('A') - 1
    # Find the index of the first uppercase letter of the class's name.
    # Example: 'Slices' returns 0.
    first_upper_class = class_name.index('A') - 1
    # Use the indices to calculate the difference of the number of lowercase
    # and uppercase letters.
    diff = abs(first_upper - first_upper_class)
    # Loop through the extensions and compare their strength.
    for i in range(1, len(extensions)):
        # Get the index of the first uppercase letter of the extension's name.
        # Example: 'AA' returns 1.
        first_upper_ext = extensions[i].index('A') - 1
        # Get the index of the first uppercase letter of the class's name.
        # Example: 'Slices' returns 0.
        first_upper_class_ext = extensions[i].index('A') - 1
        # The difference of the number of lowercase and uppercase letters is
        # equal to the strength of the extension minus the strength of the class.
        diff_ext = abs(first_upper_ext - first_upper_class_ext)
        # If the calculated difference is less than the current diff,
        # assign the new diff to the current diff and set the new extension
        # as the current one.
        if diff_ext < diff:
            diff = diff_ext
            ext_name = extensions[i]
    # Create the string to return.
    return '{0}.{1}'.format(class_name, ext_name)
