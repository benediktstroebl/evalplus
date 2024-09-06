```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i:i+m] == substring:
            count += 1
    return count

# Test case 1
print(how_many_times('aaa', 'aa'))  # Expected Output: 3

# Test case 2
print(how_many_times('', 'a'))  # Expected Output: 0

# Test case 3
print(how_many_times('aaaa', 'aa'))  # Expected Output: 3
```
This Python script defines a function `how_many_times` that finds the number of occurrences of a given substring within a larger string. The function iterates through the string characters and compares them with the substring. The function then returns the expected number of occurrences.