```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements more than once, and keeps the order of remaining elements the same. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result
```

This approach uses a set `seen` to keep track of already-seen integers in the list. The elements that are not in `seen` are added to the `result` list, and then the set is updated to reflect that this integer has been seen. This ensures that the order of elements is preserved, and duplicates are removed. 

Here is a simple test suite that can be used to verify the function:
```python
def test_remove_duplicates():
    # Basic Test
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]

    # Test with Single Unique Element
    assert remove_duplicates([1]) == [1]

    # Test with Duplicates Only
    assert remove_duplicates([2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == [2, 3, 4, 5, 6]
``` 

To test the function, the test suite can call the function with a list of integers and compare the returned list against the expected list. 

To run the test suite, the script can be executed directly in any Python environment (e.g. IDE, Terminal, Jupyter Notebook) with the appropriate indentation and spacing. 
```python
test_remove_duplicates()
``` 
This will run the test and provide feedback on whether the function behaves as expected.