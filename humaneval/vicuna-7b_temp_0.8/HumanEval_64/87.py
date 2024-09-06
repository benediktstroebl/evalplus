
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
    vowel_count = 0
    for char in s:
        if char in "aeiou":
            vowel_count += 1
        elif char == "y" and s[-1] in "aeiou":
            vowel_count += 1
    return vowel_count

def test_vowels_count():
    print(vowels_count("abcde"))
    print(vowels_count("ACEDY"))
    print(vowels_count("ay"))
    print(vowels_count("y"))
    print(vowels_count("yee"))
    print(vowels_count("aeiouy"))
    print(vowels_count("aeiouyee"))

test_vowels_count()
