```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

#Test case 1
print(how_many_times('', 'a')) # Output: 0

#Test case 2
print(how_many_times('aaa', 'a')) # Output: 3

#Test case 3
print(how_many_times('aaaa', 'aa')) # Output: 3
```
This script defines a function called `how_many_times`, which finds the number of occurrences of a given substring within a given string. It uses a specific case-based tests to validate its functionality.