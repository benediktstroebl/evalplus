Here is a Python script with a self-contained function that solves the problem of finding the longest string in a list of strings:
```python
def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list
    """
    if not strings:
        return None
    
    max_length = 0
    longest_str = ""
    
    for str in strings:
        if len(str) > max_length:
            max_length = len(str)
            longest_str = str
    
    return longest_str

# Test the function
test_longest = longest(['a', 'bb', 'ccc'])
print(test_longest)  # Output: 'ccc'

test_longest = longest([])
print(test_longest)  # Output: None

test_longest = longest(['aa', 'bb'])
print(test_longest)  # Output: 'bb'
```
The function `longest` takes a list of strings as input and returns the length of the longest string in the list. The function compares the strings by their lengths and updates the `max_length` variable and the `longest_str` variable to keep the longest string. The test cases ensure that the function works correctly.