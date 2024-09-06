```python
def count_distinct_characters(string):
    """
    Count distinct characters in a string, ignoring case.
    string = 'JErry'
    characters = set(string)
    return len(characters)

# Test the function with sample inputs
test_count_distinct_characters = count_distinct_characters 
test_count_distinct_characters('xyXYZ')  # Should return 3
test_count_distinct_characters('jerry')  # Should return 4
test_count_distinct_characters('???'# # Should return 0
```