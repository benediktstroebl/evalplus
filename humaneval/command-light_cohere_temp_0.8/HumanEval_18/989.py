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
print(how_many_times('', 'a'))  # Output: 0

# Test case 2
print(how_many_times('aaa', 'a'))  # Output: 3

# Test case 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This code defines a function **`how_many_times`** that aims to count how many times a given substring can be found in the original string, while considering overlapping substring matches. The function takes two parameters: the input string and the substring to search. It then iterates through string and checks if the substring can be found in the string by comparing the start of the current substring to the start of the original string and then comparing the rest of the substring to the remaining original string until the full length of the substring is reached.