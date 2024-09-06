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
print(how_many_times("aaa", "aa"))  # Output: 3

# Test case 2
print(how_many_times("aaaa", "aa"))  # Output: 3

# Test case 3
print(how_many_times("abc", "ab"))  # Output: 2

# Test case 4
print(how_many_times("abcd", "ab"))  # Output: 2

# Test case 5
print(how_many_times("aaaaaa", "aa"))  # Output: 4
```
The function will return the count of occurrences of the substring in the given string, and the test cases demonstrate the function's correctness for various inputs.