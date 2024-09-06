```python
# Importing the required module
from typing import List

# Defining the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    # Checking if the input list is empty
    if not strings:
        return ''
    
    # Using concatenation operator to combine strings in the list
    return ''.join(strings)

# The following tests are assumed
# They can be modified according to the user's preference
tests = [([], ''),
        ([['a', 'b', 'c']], 'abc')]

for test, result in tests:
    print(f'\n TEST: {test}\n RESULT: {result}\n')
    assert concatenate(test) == result
```

The function `concatenate` takes a list of strings as input and returns a single string as output, ensuring empty lists return an empty string. It conveniently tests the function using concrete test cases to verify the correct behavior of the function. 

To run the test suite, you can add the following command after the last line of the script (before `exit()`):
```python
test (__main__)  # Runs the test suite
``` 

This command invokes the `unittest` framework, which is a built-in testing library in Python to run the test suite. If all tests pass, you will see an indication of success returned by the interpreter, typically this will be the letter "F" followed by an indication of "OK," indicating that all tests have been completed successfully. 

To see more information about each test step, you can use the `verbose` parameter of the `unittest` framework like so: `test (__main__, verbose=True)` 

This will provide detailed information on the progress and outcome of each individual test case. 
If you prefer a different testing framework, we can discuss alternatives like `pytest`.