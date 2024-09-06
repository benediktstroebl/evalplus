```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Determine how many times a given substring can be found in the original string, 
    while not over-lapping.

    Returns the numbers of occurrences. 
    """
    string: str (original string)
    substring: str (substring to search for)
    """
    count = 0
    # Iterate over each character in the string
    for char in string:
        if char == substring:
            count += 1
    return count

# Unit tests
test_string = "aaa"
test_substring = "a"
test_count = how_many_times(test_string, test_substring)
assert test_count == 3
test_string = "abcde"
test_substring = "a"
test_count = how_many_times(test_string, test_substring)
assert test_count == 2
test_string = "spaces"
test_substring = " "
test_count = how_many_times(test_string, test_substring)
assert test_count == 3
test_string = "abc"
test_substring = "abc"
test_count = how_many_times(test_string, test_substring)
assert test_count == 0
 ```