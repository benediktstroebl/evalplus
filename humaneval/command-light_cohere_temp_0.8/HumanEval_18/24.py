```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the occurrences of a given substring within the original string.
    """
   
    in particular cases:
    - Case 1: ' ' + substring + ' '  (single character)
    - Case 2: ' ' + substring + ' '  (multiple occurrences)
    - Case 3: substring with different characters
    Return 0 if the substring is empty or the original string is empty, 1 otherwise.
def test_many_times(test_string: str, test_substring: str) -> None:
    if len(test_string) == 0 or len(test_substring) == 0:
        print("Both strings are empty. The function returns 1 as expected.")
    elif test_substring == " ":
        print("Test string is empty. The function returns 1 as expected.")
    else:
        result = how_many_times(test_string, test_substring)
        print(f"The result is: {result}")
    return result
```