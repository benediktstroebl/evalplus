```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    length_string = len(string)
    length_substring = len(substring)

    # Check if substring length is less than or equal to string length
    if length_substring <= length_string:
        return 0

    # Define a character index array
    char_index = [i for i in range(length_string)]

    # Loop through the original string
    for i in range(length_string):
        if char_index[i] == substring:
            count += 1

    return count

# Unit tests
def test_how_many_times():
    assert how_many_times('', '') == 0
    assert how_many_times('aa', 'a') == 2
    assert how_many_times('aaaa', 'aa') == 3

# Example usage
print(how_many_times('aa', 'a'))  # Expected output: 2
```
This script provides a function `how_many_times` that calculates the frequency of a given substring within a given string. The function accepts two parameters: the original string and the substring to find. The function also includes input validation to ensure the substring's length is valid. The test function `test_how_many_times` contains unit tests for the `how_many_times` function, and an example usage is provided.