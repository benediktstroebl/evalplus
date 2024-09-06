```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the string, regardless of case.
    """
    string = 'xyzXYZ jerry jerc'
    result = len([char for char in string if char.isalpha()]
    #in set('abcdefghijklmnopqr')
    return result

# Test cases
test_case1 = 'xyzXYZ'
test_case2 = 'Jerry'
test_case3 = 'jerry jurb'

assert count_distinct_characters(test_case1) == 3
assert count_distinct_characters(test_case2) == 4
assert count_distinct_characters(test_case3) == 4
```