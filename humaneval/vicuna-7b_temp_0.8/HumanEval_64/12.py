
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
    # split string on whitespace
    words = s.split()
    # iterate through each word
    for word in words:
        # check if the word ends with 'y'
        if '-y' in word:
            # add one to count
            count += 1
        # if the word doesn't end with 'y'
        else:
            # check if the word has any vowels
            count += len([word for word in word.lower().split() if any(ch in 'aeiou' for ch in word)])
    return count
