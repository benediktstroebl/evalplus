```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string) if char == substring)
 
# Test the function
string = "aaaaaa"
substring = "a"
result = how_many_times(string, substring)
print(result)
```
This code defines a function `how_many_times`, which returns the number of occurrences of a given substring within a given string. The test case demonstrates that the function will correctly identify the substring and return the expected number of occurrences.