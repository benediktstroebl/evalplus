```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel
    only when it's at the end of the word.
    """
    vowel_count = 0
    for char in s:
        if char in 'aieou':
            vowel_count += 1
        elif char == 'y' and s[-1] == 'y':
            vowel_count += 1
    return vowel_count

def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("AY") == 1
    assert vowels_count("acedy") == 3
    assert vowels_count(" Huy ") == 2
    assert vowels_count("yt") == 1
    assert vowels_count("bike") == 2
    assert vowels_count("bicycle") == 3
    assert vowels_count("ASY") == 2
    assert vowels_count("sfjlks") == 0

test_vowels_count()
```

This script includes a test suite with various inputs (`test_vowels_count`) to ensure the `vowels_count` function's correctness. Increase the test coverage by adding more test cases to verify different word scenarios.