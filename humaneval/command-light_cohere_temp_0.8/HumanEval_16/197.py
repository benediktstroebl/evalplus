```python
def count_distinct_characters(string: str) -> int:
    """
    Count distinct characters in a given string, regardless of case.
    return: 
    # Convert string to lowercase and remove all non-alphanumeric characters
    str = ''.joinist(str, str.allyalpha())
    str = ''.join(str)
    # Count distinct characters
    return len([char for char in str if char.isalpha()] )
return
```
This function converts all characters to lowercase and removes all non-alphanumeric characters, then counts the number of distinct characters remaining. The time complexity is O(n) and the space complexity is O(1) since we are simply using the string.