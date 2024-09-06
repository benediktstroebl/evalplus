```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string]

# Test case: Returns all prefixes of 'abc'
test_case = "abc"
result = all_prefixes(test_case)
assert len(result) == 3  # Ensure list length is correct
assert result == ['a', 'ab', 'abc']  # Check if list content is correct
print("Test case passed!")
``` 
This code defines a function all_prefixes that returns a list of all prefixes of the input string. It uses list comprehension to iterate over each character in the string and creates a new string with each character, which is then added to the result list. 

This function is self-contained, and it can be used to solve the problem of finding all prefixes of a given string.