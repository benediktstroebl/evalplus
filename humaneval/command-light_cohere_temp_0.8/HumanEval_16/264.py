```python
def count_distinct_characters(string):
    """ 
    Returns the count of distinct characters in the string (case insensitive) 
"""  
    char_count = set(string).count(c) for c in char_count if char_count.count(c) == 1  
    return len(char_count)

# Example usage
test_string = "xyzXYZ jerry yes indeed"
assert count_distinct_characters(test_string) == 3
```