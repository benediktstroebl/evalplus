```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the string, regardless of case.
    """
    string = 'xyzXYZ'
    return len([char for char in string if char.isalpha()]
 }

#Test cases
test_string = 'Jerry'
assert count_distinct_characters(test_string) == 4

test_string2 = 'hello'
assert count_distinct_characters(test_string2) == 5
```
This Python script defines a function called `count_distinct_characters` that calculates and returns the number of distinct characters in a given string. The function uses a list comprehension to filter and count only the alphabetical characters in the string. The test cases demonstrate the method's expected behavior.