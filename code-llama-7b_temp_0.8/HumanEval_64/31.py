
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
    vowels = "aeiouAEIOU"
    vowels_dict = {}
    for v in vowels:
        vowels_dict[v] = 0
    count = 0
    for i in s:
        if i in vowels_dict:
            vowels_dict[i] += 1
        if i == 'y' and i == s[-1]:
            count += 1
    return count + sum(vowels_dict.values())

