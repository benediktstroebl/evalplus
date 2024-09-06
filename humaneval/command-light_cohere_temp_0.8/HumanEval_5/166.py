```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_data = [1, 2, 3, 4, 5]
test_delimiter = 4
test_expected = [1, 5, 9, 13, 17]

def test_inperse():
    actual = intersperse(test_data, test_delimiter)
    assert actual == test_expected

test_success = test_inperse()
print("Tests passed: ", end='')
print(test_success)
```

This code defines a function `intersperse` that takes a list of numbers and a delimiter as input, and returns a list of interspersed numbers. It then provides a two test cases, which pass the expected output and the `test_inperse` function that checks the correctness of the `intersperse` function.  The test_inperse() and verifies if the test cases pass.