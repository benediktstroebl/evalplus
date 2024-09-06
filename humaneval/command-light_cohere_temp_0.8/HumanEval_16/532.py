Here is a self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c not in set(string)})

# Test the function with some examples
test_count_distinct_characters = count_distinct_characters 
test_count_distinct_characters('xyzXYZ')  # Should return 3
test_count_distinct_characters('Jerry')  # Should return 4
test_count_distinct_characters('abcABC123')  # Should return 5
```  This function leverages Python's set and list-based techniques to efficiently find the number of unique characters. It returns the  an integer count of unique characters, which is a standard and efficient way to achieve this task.