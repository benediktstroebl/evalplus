

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
    # Get the list of vowels
    vowels = 'aeiouAEIOU'
    
    # Create a set of vowels
    vowel_set = set(vowels)
    
    # Get the list of characters in the text
    characters = list(text)
    
    # Initialize a counter variable to keep track of the number of occurrences of each character
    count = {}
    
    # Iterate over each character in the text
    for char in characters:
        # If the character is a vowel, increment the counter
        if char in vowel_set:
            count[char] += 1
    
    # Iterate over each character in the text
    for char in characters:
        # If the character has not been seen before, add it to the count and add it to the dictionary
        if char not in count:
            count[char] = 1
        # If the count of the character is greater than 1, remove the character
        if count[char] > 1:
            del count[char]
            del characters[count.index(char)]
    
    # Iterate over each character in the text
    for char in characters:
        # If the character has not been seen before, add it to the count and add it to the dictionary
        if char not in count:
            count[char] = 1
        # If the count of the character is greater than 1, remove the character
        if count[char] > 1:
            del count[char]
            del characters[count.index(char)]
    
    # Return the modified text
    return ''.join(char for char in characters if char in count)
