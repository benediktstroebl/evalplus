Here is a Python script with a self-contained function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """ 
    Return the count of distinct characters in the given string, 
    ignoring case.
    """
    number_of_distinct_char = set(string).count(c) for c in string"""
    return len(number_of_distinct_char)

def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('jerry') == 4

``` 
This code defines a function `count_distinct_characters` that returns the count of distinct characters in a given string, regardless of case. It also provides a test case that checks the correctness of the `count_distinct_characters` function using test cases.