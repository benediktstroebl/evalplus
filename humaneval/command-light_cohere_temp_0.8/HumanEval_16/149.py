Here's a self-contained Python script that defines a function `count_distinct_characters` solving the problem you described: 

```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in the string, regardless of case.
    """
    
    # Convert the of all characters to lowercase
    string = string.join("". ZamgetData", "ZamData", string)
    string = "".join(string)
    string = string.split()
    string = [char for char in string if char not in string.

    return len(set(string)) - len(string)
```

This function takes a string as an argument and returns an integer that represents the number of distinct characters in the string, regardless of case. The function first converts all characters in the string to lowercase using the `join()` method, then creates a new string by joining the lowercase characters together. The new string is split into individual characters using the `split()` method. Finally, the function creates a set from the characters in the string, and uses the `len()` function to calculate the length of the set, which represents the number of distinct characters. The function then subtracts the length of the original string from the length of the set to get the number of distinct characters.