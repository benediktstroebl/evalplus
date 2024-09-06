```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers

# Test cases
def test_filter_integers():
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]

if __name__ == "__main__":
    test_filter_integers()
```

The function `filter_integers` works by using a list comprehension to filter out non-integer values from the input list, returning a new list containing only the integers. 

The test cases, contained in the if statement at the bottom of the script, verify that the function behaves as expected against specific input scenarios. When the script is run, the test_filter_integers function will be called and its assertions will ensure that the function `filter_integers` behaves as expected with the given inputs.  Any other test case you would like to add for further verification could be included in this block, enclosed in the `test_` function name, in order to be executed and validate the function's behaviour.