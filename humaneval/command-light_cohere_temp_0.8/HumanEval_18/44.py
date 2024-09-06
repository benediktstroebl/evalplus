```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find how many times a given substring can be found in the original string, 
    counting overlapping occurrences.
    Returns the how many string is divided into substrings, and counts how many occurrences of each 
    unique substring are found.
    """
    loops through string, using substring as a filter, and counts the occurrences using 
    a dictionary.
def how_many_times(test_string, test_substring): 
    """

    :param string: The input string
    :param substring: The substring to find
    :return: number of occurrences of the substring in the string

test_string = "aaaabbbcccddaaaa"
test_substring = "a"
result = how_many_times(test_string, test_substring)
print(result)  # expected output: 3
```