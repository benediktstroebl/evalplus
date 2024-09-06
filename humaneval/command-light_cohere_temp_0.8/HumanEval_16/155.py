```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

# Unit tests for the function
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('JER') == 4
    assert count_distinct_characters(' jerry ') == 4
    assert count_distinct_characters('   jerry  ') == 4
``` 
This code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. The function uses the string. The set() method is used to convert the characters into a set, and the len() function is then used to count the number of elements in the set. 
The function is then tested with various strings in the `test_count_distinct_characters` function.