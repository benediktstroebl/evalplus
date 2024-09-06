```python
def count_distinct_characters(string):
    """ 
    Returns the number of distinct characters in the given string (case insensitive)  
    
    :param string: str, the input string to check
    :return: int, the number of distinct characters
    """
    set = set(string)
    return len(set)

# Unit tests
string1 = "xyzXYZ"
string2 = "jerry"
string3 = " Jerry"

assert count_distinct_characters(string1) == 3
assert count_distinct_characters(string2) == 4
assert count_distinct_characters(string3) == 3 

```