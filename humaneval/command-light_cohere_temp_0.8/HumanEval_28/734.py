```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    Args:
        strings (List[str]): A list of strings to concatenate

    Returns:
        str: The concatenated string
    """
    if not strings:  # Empty list
        return ''

    # Initialize a new string to store the concatenation
    result = ''
    for s in strings:
        # Concatenate the current string to the result
        result += s

    return result

# Unit tests
test_concatenate = []
test_concatenate.append(["a", "b"], "ab")
test_concatenate.append(["c", "d"], "cd")
test_concatenate.append(["e", "aa"], "una")

# Test cases
concatenate_results = []
for test in test_concatenate:
    concatenate_results.append(concatenate(test))

print(concatenate_results)
 ``` 
The provided Python script defines a function called `concatenate` that takes a list of strings as input and returns the concatenated string. 

The function first checks if the input is an empty list, in which case it returns an empty string. 

Then, for each string in the input list, it appends the string to the result string using the `+` operator. 
The test cases are defined, which test the `concatenate` function with different input strings. 

The test results are stored in the `concatenate_results` list, which is then printed to the console.