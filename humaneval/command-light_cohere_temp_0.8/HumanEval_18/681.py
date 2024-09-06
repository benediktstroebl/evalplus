```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string if char == substring)
    
#Test case 1
print(how_many_times('', 'a'))  # Output: 0

#Test case 2
print(how_many_times('aaa', 'a'))  # Output: 3

#Test case 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
This Python code provides a function named **`how_many_times`** that aims to determine the count of occurrences of a given substring within a given string. The function utilizes a simple approach: it employs a generator expression to iterate over each character in the input string, counting instances of the substring. This function is expected to have a clear and concise design, effectively solving the problem of counting occurrences of a substring within a larger string.