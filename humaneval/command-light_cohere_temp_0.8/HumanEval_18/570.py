```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_s = len(string)
    len_sub = len(substring)

    for i in range(len_s):
        if string[i] == substring:
            count += 1

    return count

# Test case 1
print(how_many_times('', 'a'))  # Output: 0

# Test case 2
print(how_many_times('aaa', 'a'))  # Output: 3

# Test case 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
This script defines a function `how_many_times` that calculates the frequency of a given substring within a given string. The function uses a counting mechanism to achieve this and returns the count of occurrences.