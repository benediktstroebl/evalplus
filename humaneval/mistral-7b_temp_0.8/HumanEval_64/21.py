
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # your code here
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    #add the other vowels in the dictionary, so we can add up later
    vowels['y'] = 0
    #loop through each letter in the string
    for letter in s:
        #add to the dictionary, if it is a vowel
        if letter in vowels:
            vowels[letter] += 1

    #add up the values of the vowels
    total = 0
    for value in vowels.values():
        total += value
    return total

