Here's a self-contained Python function that finds all prefixes from shortest to longest of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    # Use Python's built-in "list" to store our results
    prefixes = []
    # Loops through each character in the string
    for i in range(len(string)):
        # Append each character to our prefixes list
        prefixes.append(string[i])
    return prefixes
```
This function uses the built-in list function to create a new list that will store the prefixes.

Here's a sample test to run the function:
```python
# Test
test_string = "abc"
result = all_prefixes(test_string)
print(result)
```
This will print the list of all prefixes from shortest to longest of the test string.