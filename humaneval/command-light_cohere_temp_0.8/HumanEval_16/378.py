```python
def count_distinct_characters(string):
    """ 
    Return the number of distinct characters in the string, regardless of case.
    """
    string = 'xyzXYZ abcDef456 jerry123'
    return len([char for char in string. distinct if not char.isupper() and distinct_ 
    return 
    
    """
    test case 1:
    assert count_distinct_characters('xyzXYZ') == 3
    test case 2:
    assert count_distinct_characters('Jerry') == 4
```