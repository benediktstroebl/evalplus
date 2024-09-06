```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)

    for i in range(n):
        if string[i] == substring:
            count += 1

    return count

# Test cases
test_string = "aaaaaaa"
test_substring = "a"

result = how_many_times(test_string, test_substring)
print(result)  # Output: 3

test_string = "hello"
test_substring = "o"

result = how_many_times(test_string, test_substring)
print(result)  # Output: 2

test_string = "abc"
test_substring = "a"

result = how_many_times(test_string, test_substring)
print(result)  # Output: 2
```