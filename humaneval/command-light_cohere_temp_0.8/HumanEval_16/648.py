```python
def count_distinct_characters(string: str) -> int:
    return len(string.find(x for x in string.string())
```. could be used to achieve a problem of counting distinct characters in the given string. 

This function leverages the `find()` method which returns an iterator for the first occurrence of each element in the string.