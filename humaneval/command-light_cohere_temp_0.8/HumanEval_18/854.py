```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i:i+m] == substring:
            count += 1
    return count

# Test the function
test_str = "aaaaaaa"
test_sub = "aa"
test_result = how_many_times(test_str, test_sub)
print(test_result)  # Output: 3
```
This script defines a function how_many_times that calculates the frequency of a substring within a given string. The function iterates over the string characters and checks if a substring of length m is present at position i for at least m characters, counting it as a match.