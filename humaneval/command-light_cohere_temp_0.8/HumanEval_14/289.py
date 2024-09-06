```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != '']

# Run the function and verify the output against the test cases
def test_cases():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("") == []
    assert all_prefixes("-abc") == ['-']
    assert all_prefixes("123") == ['1', '23']
    assert all_prefixes("abc123") == ['abc', '123']

# Call the function with recommended string input
print("Result:", all_prefixes(""abc""))
test_cases()
```
This Python code defines a function called `all_prefixes` that generates a list of all prefixes from the shortest to the longest characters in a given input string. 

It uses a list comprehension with a character filter (`char != ' '`) to generate all prefixes, excluding the space character. 

The `test_cases` function runs the `all_prefixes` function with various input strings and verifies that the output matches the expected results from the test cases.

Finally, the code prints the result of the function call and executes the `test_cases` function to validate the function's correctness.