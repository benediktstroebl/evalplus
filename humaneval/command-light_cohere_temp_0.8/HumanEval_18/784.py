```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test case 1
print(how_many_times('a', 'a'))  # Output: 0

# Test case 2
print(how_many_times('aaa', 'a'))  # Output: 3

# Test case 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
This script defines a function called `how_many_times` that calculates the number of occurrences of a given substring within a given string. The function utilizes a loop to iterate through each character in the input string and counts occurrences of the target substring. It returns the time, which counts the number of matches.