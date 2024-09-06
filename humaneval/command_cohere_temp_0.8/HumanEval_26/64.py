```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen and not seen.add(num):
            result.append(num)
    return result
```

This script defines a function called `remove_duplicates` which takes a list of integers as input and returns a list of unique integers. Inside the function, it tracks seen integers using a `set` and appends only unique occurrences of integers to the `result` list.

Here is a test case to ensure the function is working correctly:
```python
def test_remove_duplicates():
    # List with duplicate integers
    num_list = [1, 2, 3, 2, 4]
    expected_result = [1, 3, 4]
    assert remove_duplicates(num_list) == expected_result
``` 

The test case creates a list of integers including duplicates, passes it into the `remove_duplicates` function, and compares the output with the expected unique list. 

To run the test, you can add this code to a Python file and execute the file, and the test will pass. 
```python
test_remove_duplicates()
``` 
You can also use an IDE or testing framework to automate and organize your tests more systematically.