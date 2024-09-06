```python
def count_distinct_characters(string):
    """ Returns the number of distinct characters in the string (case-insensitive)"""
    return len([c for c in string.iad() if c.isalpha()])
 regular expression? difference.

def test_distinct_characters(string):
    return count_distinct_characters(string) == len(string)
```

In this script, the `count_distinct_characters` function uses the `isalpha()` method to determine if each character is an alphabetic, and then counts the number of distinct characters. The test_distinct_characters function verifies the accuracy of the `count_distinct_characters` function against various inputs.