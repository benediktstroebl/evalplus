```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Returns the number of vowels in a string s,
    including special case 'y' as a vowel at the end of the word."""
    import re

    return sum(1 for char in s if char in 'aeiou' or (char == 'y' and s[-1] == 'y'))

def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("bach") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("edy") == 1
    assert vowels_count("esy") == 2
    assert vowels_count("asy") == 1
    assert vowels_count("aaasy") == 3
    assert vowels_count("Aasy") == 2
    assert vowels_count("ASY") == 1
    assert vowels_count("axxyyyxx") == 6
    assert vowels_count("axyzy") == 3
    assert vowels_count("aoy") == 1
    assert vowels_count("Ouy") == 2
    assert vowels_count("ouyt") == 1  # this is y, not u
    assert vowels_count("ouytz") == 2  # this is y, not u
    assert vowels_count("iuy") == 2  # this is y, not i
    assert vowels_count("eu") == 2
    assert vowels_count("OO") == 2
    assert vowels_count("OOy") == 3
    assert vowels_count("AO") == 1
    assert vowels_count("AOy") == 2
    assert vowels_count("AI") == 1
    assert vowels_count("AIy") == 2
    assert vowels_count("AY") == 1
    assert vowels_count("IY") == 1
    assert vowels_count("iry") == 2
    assert vowels_count("LEASY") == 4
    assert vowels_count("LEasy") == 3
    assert vowels_count("easy") == 2
    assert vowels_count("LEAY") == 2
    assert vowels_count("LEY") == 1
    assert vowels_count("LEOY") == 3
    assert vowels_count("LEO") == 2
    assert vowels_count("LEAI") == 2
    assert vowels_count("LEAIy") == 3
    assert vowels_count("LEAYy") == 3
    assert vowels_count("LEIY") == 2
    assert vowels_count("LEiry") == 3
    assert vowels_count("LAasy") == 3
    assert vowels_count("LAasyy") == 4
    assert vowels_count("LAasyyy") == 5
    assert vowels_count("LLasy") == 3
    assert vowels_count("LLasyy") == 4
    assert vowels_count("LLasyyy") == 5
    assert vowels_count("Lasy") == 2
    assert vowels_count("Lasyy") == 3
    assert vowels_count("Lasyyy") == 4
    assert vowels_count("ALasy") == 3
    assert vowels_count("ALasyy") == 4
    assert vowels_count("ALasyyy") == 5
    assert vowels_count("slasy") == 3
    assert vowels_count("slasyy") == 4
    assert vowels_count("slasyyy") == 5
    assert vowels_count("sLasy") == 3
    assert vowels_count("sLasyy") == 4
    assert vowels_count("sLasyyy") == 5
    assert vowels_count("SLasy") == 3
    assert vowels_count("SLasyy")