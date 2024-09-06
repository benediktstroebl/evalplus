```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string in the list.
    Parameters:
    strings (List[str]): A list of strings.
    Returns: The length of the longest string in the list.
    Returns: None if empty list.
    """
    longest([])   
    """

    # Call the function with an empty list
    if not strings:
        return None

    # Sort the list in ascending order
    strings.sort()
    string in the list and return the first one
    # since all strings have the same length
    return next(strings)[0]

# Unit tests
test_longest = []
test_longest.append("['a', 'b', 'c']")
test_longest.append("['abc', 'ab']")
test_longest.append("['', 'abc'])")
test_longest.append(None)

# Verify function
longest(test_longest)

``` 
This solution defines a function called `longest` that takes a list of strings as input and returns the length of the longest string in the list. It also implements a tests to verify that the function works as expected.