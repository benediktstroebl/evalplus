
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

    # Create a set to store unique vowels
    vowels = set()

    # Create a list to store the count of each vowel
    vowel_count = [0] * 5

    # Iterate through all the characters in the string
    for char in s:
        if char in "aeiou":
            vowels.add(char)
            vowel_count[ord(char) - ord("a")] += 1

    # Add 'y' to the count if it is at the end of the word
    if s[-1] == "y":
        vowels.add(s[-1])
        vowel_count[ord(s[-1]) - ord("a")] += 1

    # Return the count of vowels
    return len(vowels)
