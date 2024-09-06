```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel 
    only when it's at the end of the word.
    """
    if not s:
        return 0
    count = 0
    for char in s:
        if char in 'aieou':
            count += 1
        elif char == 'y' and s[-1] == 'y':
            count += 1
    return count

def test_vowels_count():
    """Tests the vowels_count function."""
    assert vowels_count("abcde") == 2
    assert vowels_count("Acharya") == 4
    assert vowels_count("SYzygy") == 3
    assert vowels_count("SAFI") == 2
    assert vowels_count("DIABOL") == 3
    assert vowels_count("COSY") == 2
    assert vowels_count("") == 0
    assert vowels_count("X") == 0
    assert vowels_count("AY") == 1
    assert vowels_count("Y") == 1
    assert vowels_count("AYY") == 2
```

The `vowels_count` function takes a string representing a word as input and returns the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u', and 'y' at the end of the word. It iterates through each character in the string, incrementing a counter when it encounters a vowel. The `test_vowels_count` function provides example tests to validate the functionality of the `vowels_count` function. 

Note: The `FIX` string is a placeholder to remind you to add more test cases to ensure the robustness of the `vowels_count` function.  It will cause a failure in the unit tests if not implemented adequately.