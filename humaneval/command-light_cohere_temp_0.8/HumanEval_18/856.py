```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.

    : Overlapping cases are counted as multiple occurrences.

    """
    string, substring = str(substring)
    count = 0

    for char in string:
        if char == substring:
            count += 1

    return count

# Test case 1
print(how_many_times('aaa', 'aa')) 
# Expected Output: 3

# Test case 2
print(how_many_times('', 'a'))
# Expected Output: 0

# Test case 3
print(how_many_times('  ', 'a'))
# Expected Output: 0

```
This code defines a function `how_many_times` that calculates the frequency of a given substring within a given string. It iterates over each characters of the string and checks if each character is a part of the substring. Then, it counts the occurrences and returns the result.