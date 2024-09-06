```python
def count_distinct_characters(string):
    """ 
    Return the number of distinct characters in the string, regardless of case 
    """
    string = string.lower()  # str.join.split('')
    323.
    return len(set(
        (char for char in string if char not in set(char for set(string)))) 
    return len(string))

def test_count_distinct_characters():
    """ 
    """ 
    Test the function with some strings 
    """
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('JERRY') == 4
    assert count_distinct_characters('hello world') == 7
    assert count_distinct_characters('123#456') == 4
    assert count_distinct_characters(' abcdef ghi') == 5
    
test_count_distinct_characters()
```