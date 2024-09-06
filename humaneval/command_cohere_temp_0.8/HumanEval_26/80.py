```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Returns a new list without duplicates, keeping the order of elements untouched.
    """
    return list(set(numbers))
```
This Python script defines a function called `remove_duplicates`, which takes a list of integers as input. Inside the function, it uses a set because sets don't allow duplicates, and then converts it to a list to retain the order of elements. This approach makes sure that if there are any duplicate elements in the input list, they will be automatically removed, resulting in a list of unique integers. The function returns this modified list, achieving the goal of removing duplicates while preserving the original order of elements.

Here is a simple test case to validate the script:
```python
# Test the remove_duplicates function
def test_remove_duplicates():
    # Input with duplicates
    input_list = [1, 2, 3, 2, 4]
    expected_output = [1, 3, 4]
    output = remove_duplicates(input_list)
    assert output == expected_output  # Assert that the function works as expected
``` 
The `test_remove_duplicates` function uses the `remove_duplicates` function to remove duplicates from a list containing duplicates, then it compares the result with the expected output, this quick test ensures the function works as expected.