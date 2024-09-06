Here's a self-contained Python script that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Define the rescaling function
    numbers_rescaled = [x / (max(numbers) - min(numbers)) + min(numbers) for x in numbers]
    return numbers_resc

# Test cases
def test_rescale_to_unit():
    test_cases = [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 0.0, 0.5, 0.0, 0.0, 0.0, 0.0], 0.1, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0], 0.99, 0.0, 0.0, 0.0], 0.2, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0], 0.0, 0.0]
   0.0, 0.0],
       5, 0.0], 0)

    test_cases = [
        test_case_list = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 75.0, 1.0])
        test compare_specifics=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            test_cases[test_rescale_to_unit()]
    assert test_rescale_to_unit.eq0 == [case_rescaled]
    assert test_rescale_to_unit.1 == case_rescaled
   0
    assert test_rescale_to_unit.2 == case_rescaled
   0
    assert test_rescale_to_unit.3 == case_rescaled
   0
    assert test_rescale_to_unit.4 == case_rescaled
   0
    assert test_rescale_to_unit.5 == case_rescaled
   0
    assert test_rescale_to_unit.6 == case_rescaled
   0
    assert test_rescale_to_unit.7 == case_rescaled0
   
```

This script defines a function called `rescale_to_unit` that takes in a list of numbers and returns a new list where each number has been rescaled. The test case section includes a series of test cases to verify the correctness of the `rescale_to_unit` function.  The main idea is to test the function on a variety of scenarios, and check if the output of the function matches the expected result.