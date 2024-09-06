```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string while avoiding overlapping occurrences.
    >>> string: input is the string in which substring will be searched
    >>> substring: input is the substring to search for in the string
    """
    occurrences = [i for i, char in enumerate(string) if char == substring]
    return len(occurrences)

# Test cases
test_string = "aaa"
test_substring = "a"
test_count = how_many_times(test_string, test_substring)
print("Test string:", test_string)
print("Test substring:", test_substring)
print("Test Count:", test_count)

test_string = "hello world"
test_substring = "l"
test_count = how_many_times(test_string, test_substring)
print("Test string:", test_string)
print("Test substring:", test_substring)
print("Test Count:", test_count)

```