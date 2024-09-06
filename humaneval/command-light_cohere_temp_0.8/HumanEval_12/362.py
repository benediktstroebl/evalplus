```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the length of the longest string in the list.
    """
    # Initialize the string length as 0
    longest_length = 0

    # Iterate over the list
    for string in strings:
        # Compare string length
        if len(string) > longest_length:
            longest_length = len(string)

    # Return the length of the longest string
    return longest_length

# Test cases
test_longest = []
test_longest.push_list(['a', 'b', 'c'])
test_longest.push_list(['a', 'bb', 'ccc'])
test_longest.push_string('a')

# Run the function on test cases
print(longest(test_longest))

``` 
The provided code defines a Python script with a self-contained function called `longest()`.Bank on a list of strings, it returns the length of the longest string in the list. The function first initializes the string length as 0 and then iterates over the list, comparing the length of each string with the current longest string length. The longest string length is then stored in the `longest_length` variable and returned from the function. 

The test cases are defined in the `test_longest` list, which is then populated with a list of strings, a string, and a string of the same length. The `longest` function is then run on the `test_longest` list, and the results are printed to the console.

This code demonstrates the functionality of the `longest` function, which efficiently computes the length of the longest string in a given list of strings.