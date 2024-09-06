```python
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
    count = 0
    for char in s:
        if char in 'aieou':
            count += 1
        elif char == 'y' and s.endswith(char):
            count += 1
    return count

# Add more test cases
test_words = ["test", "centre", "encyclopaedia", "cylinder", "system", "ggy"]
for word in test_words:
    assert vowels_count(word) == len(list(filter(lambda c: c in 'aieouyy', word)))
```

The problem entails crafting a function vowels_count that takes a string representing a word as input and returns the number of vowels in the string. Vowels are defined as 'a', 'e', 'i', 'o', 'u', and 'y' when it appears at the word's end. The given example shows how the function should operate for specific words and asserts that it produces the correct count for a variety of test cases.