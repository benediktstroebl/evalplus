

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
    #convert text to lowercase
    text = text.lower()
    #create a string with all possible vowels
    vowels = 'aeiouAEIOU'
    #create a set to store the frequency of each letter
    letter_freq = set()
    #iterate through each character in the text
    for char in text:
        #if the character is a vowel, add it to the set of frequent vowels
        if char in vowels:
            letter_freq.add(1)
        #if the character is not a vowel, add it to the set of frequent non-vowels
        else:
            letter_freq.add(1)
    #sort the set of frequent characters in descending order of frequency
    letter_freq = sorted(letter_freq, reverse=True)
    #loop through the sorted set of frequent characters
    for char in letter_freq:
        #if the frequency is greater than 1, remove the vowel from the text
        if char > 1:
            text = text.replace(char, '')
    return text