```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    length_string = len(string)
    length_substring = len(substring)

    # Loop through each position in the string
    for i in range(length_string):
        if string[i] == substring:
            count += 1
        # Check if the substring has reached the end of the string
        if i == length_string:
            break

    return count

# Test cases
test_string = "aaaaaaa"
test_substring = "aa"

result = how_many_times(test_string, test_substring)
assert result == 3

# You can add more test cases here to further validate your function
```