
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

    # Your code here.

    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    word = s.lower()
    for letter in word:
        if letter in vowels:
            vowel_count += 1
    if len(word) > 0 and word[-1] == "y":
        vowel_count -= 1
    return vowel_count
