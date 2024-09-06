
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
    from string import ascii_letters as letters
    # Makes a dictionary of the letters and their count
    letter_count = {i:0 for i in letters}
    # Iterate over each letter in the class_name
    for char in class_name:
        # If the letter is in the dictionary add one to the letter's count
        if char in letter_count:
            letter_count[char] += 1
    # Sort the dictionary by values descending
    sorted_letter_count = {k: v for k, v in sorted(letter_count.items(), key=lambda item: item[1], reverse=True)}
    # Check if the length of the sorted dictionary is less than 1
    if len(sorted_letter_count) < 1:
        return str(class_name)
    # Get the first key in the dictionary
    strongest_extension = sorted_letter_count.popitem()[0]
    # Iterate over the sorted dictionary
    for key in sorted_letter_count.keys():
        # Subtract the count of the first key from the count of the current key
        strength = sorted_letter_count[key] - strongest_extension
        # If the strength is greater than 0 set the new strength as the new strongest
        if strength > 0:
            strongest_extension = key
    # Return the class_name concatenated with the strongest extension
    return str(class_name + '.' + strongest_extension)
