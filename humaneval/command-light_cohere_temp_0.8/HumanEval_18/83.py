```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    # Count the goal is to find all occurrences of substring in the string and return count
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
test_string = "aaaaaaa"
test_substring = "a"

result = how_many_times(test_string, test_substring)
print("Number of times a substring can be found:", result)

test_string = "hello world"
test_substring = "ello"

result = how_many_times(test_string, test_substring)
print("Number of times a substring can be found:", result)
```
The function `how_many_times` takes two arguments: a string and a substring. The function then uses a loop to iterate over the characters in the string. The function compares each character to the substring, and if a match is found, increments the count.