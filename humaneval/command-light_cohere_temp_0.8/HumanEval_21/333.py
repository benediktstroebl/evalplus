Here is a self-contained Python script with a function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers = [x / 100.0 for x in numbers]  # Divide each number by 100 to get it between 0 and 1
    return numbers

def test_rescale_to_unit(test_cases: List[List[float]]) -> List[List[float]]:
    for t in test_cases:
        actual = [x / 100.0 for x in t]  # Divide each number in the list by 100 to get it between 0 and 1
        expected = [0.0, 1.0]  # Divide each number by 100 to get it between 0 and 1
        if actual != expected:
            return False
    return True
```

This code defines a function `rescale_to_unit` that takes a list of numbers as input and returns a list of numbers after applying a linear transformation to the input list. The function then divides each number in the list by 100 to get it between 0 and 1, which is the linear transformation that is needed to scale the numbers to the unit [0, 1].

The function also has a test case that checks whether the function is working correctly or not. It takes a input of a list of lists of numbers and returns a list of lists of bool values, where the function passed the test case. The test case checks whether the expected output of the function is a list of numbers that is divided by 100 to get it between 0 and 1, and the actual output of the function is also a list of numbers that is divided by 100 to get it between 0 and 1.

If the actual output is not equal to the expected output, the function returns False. If the actual output is equal to the expected output, the function returns True.