

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    # Create a list of vowels
    vowels = 'aeiouAEIOU'
    # Create a list of vowel counts
    vowel_counts = [0] * 6
    # Loop through each character in the string
    for char in text:
        # If the character is a vowel, increment the count for that vowel
        if char in vowels:
            vowel_counts[vowels.index(char)] += 1
    # If the length of the vowel_counts list is less than 6,
    # append a zero to the end of the list
    for i in range(6 - len(vowel_counts)):
        vowel_counts.append(0)
    # Create a new string with the vowels removed
    new_string = ''
    for i in range(len(vowel_counts)):
        if vowel_counts[i] > 0:
            new_string += char
    return new_string
