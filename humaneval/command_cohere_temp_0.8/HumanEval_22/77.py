```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It utilizes Python's list comprehension feature along with the `isinstance()` function to filter out non-integer elements from the input list. 

To ensure functionality, test the script with the following sample inputs:
```python
# Test with a list of various elements
sample_inputs = [
    ['a', 3.14, 5, 'cat'], 
    [1, 2, 3, 'abc', {}, []],
    [4, 5.2, 7.7, {1: 2, 3: 4}],
]

expected_outputs = [
    [5],
    [1, 2, 3],
    [4, 5, 7],
]

for ii, (inputs, expected) in enumerate(zip(sample_inputs, expected_outputs)):
    result = filter_integers(inputs)
    assert result == expected, \
        f"For inputs {inputs}, expected {expected} but got {result}"
``` 

The test code provides an array of sample inputs along with the expected output for each. The primary test function iterates over each entry, runs the `filter_integers` function on the input, and compares the result against the expected output. If the two do not match, the test fails and an error message is generated.