Here is a self-contained Python script with a function that finds the number of times a given substring can be found in another string, while avoiding external dependencies:
```python
def how_many_times(str1: str, str2: str) -> int:
    return len(str1.findall(str2))
```
This function takes two strings as input and returns the number of times the given substring can be found in the original string. It utilizes the findall function to locate each occurrence of the substring in the string. It is a built-in this way, the function is self-contained and can be easily reused without requiring external dependencies or additional code.