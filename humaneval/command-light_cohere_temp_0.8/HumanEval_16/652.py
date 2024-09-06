```python
def count_distinct_characters(string: str) -> int:
    return len([c for c in string.
    if c not in 'abcdefghijklmnopqr'
    ):
        return 0
    else:
        return 1

# Test cases
test_distinct_characters = """
def test_distinct_characters():
    string = 'xyzXYZ'
    assert count_distinct_characters(string) == 3

def test_empty_string():
    string = ''
    assert count_distinct_characters(string) == 0

def test_only_upper():
    string = 'jerry'
    assert count_distinct_characters(string) == 4
```
This Python script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. 

It uses a list comprehension to iterate over each character in the string, and if the character is not found in the set of lowercase English letters, the function returns 0, indicating that there are no distinct characters. 

This function is then tested using three different cases: a string with multiple distinct characters, an empty string, and a string with only uppercase characters.