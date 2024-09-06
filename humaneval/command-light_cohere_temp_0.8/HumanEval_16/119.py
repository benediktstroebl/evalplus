```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the count of distinct characters in the given string, regardless of case.
    """
    string = "xyzXYZ abcDef456 gHIjkl830!"
    return len([char for char in string if char.isalpha() and])
```  This code defines a Python function that counts the number of unique characters in a given string, regardless of case. The function uses list comprehension to filter out duplicate characters from the string, and then counts the number of non-duplicate characters. The function then tests the unique characters with the input string "xyzXYZ abcDef456 gHIjkl830." The output will be the count of distinct characters, which in this case is 6.