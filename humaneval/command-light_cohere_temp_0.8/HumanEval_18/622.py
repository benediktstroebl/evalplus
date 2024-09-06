Here is a self-contained Python script that defines a function to solve the problem of finding the number of times a given substring can be found in a string:
```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This function takes two parameters: a string and a substring. The function then uses the find method to search the substring in the string. This method returns the the a list of all the positions the substring was found, which we then convert to an integer using len.