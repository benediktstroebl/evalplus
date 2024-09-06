Here is a self-contained Python script that defines a function that finds the number of times a given substring can be found in the original string while avoiding overlapping cases:

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string without overlapping.
    """
   
    string: str
    substring: str

    # Ensure substring is valid and not empty
    if not substring:
        return 0

    # Find all occurrences of substring in string
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1

    return count
```

This function uses a loop to iterate over each character in the string and counts the number of occurrences of the substring. 

This is a straightforward and efficient way to solve the problem without relying on external libraries or functions.