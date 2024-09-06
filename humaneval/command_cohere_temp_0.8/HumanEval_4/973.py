Here's a Python script with a self-contained function that solves the problem you've outlined, along with a sample test to demonstrate its usage:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

def test_mad():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert mean_absolute_deviation([0.5, 1.0, 1.5, 2.0]) == 0.5
    assert mean_absolute_deviation([-1.0, 0.0, 1.0, 2.0]) == 1.0
    assert mean_absolute_deviation([10, 20, 30, 40]) == 15 

if __name__ == "__main__":
    pytest.main(['-v', '-s', '-x', '--pdb', '-c', 'test_mad.py'])
```
This script employs the `numpy` library to provide a more efficient implementation of the Mean Absolute Deviation (MAD) calculation. The `test_mad()` function showcases the feature by conducting three distinct tests and it is encapsulated within a `pytest` module to enable an automated test runner. To examine the function's correctness, we have also included a `__main__` block that facilitates a test runner when the script is executed directly. 

You can use this script as a self-contained solution to calculate the MAD for any list of numbers. To run the tests, simply execute the script from your Python environment, and the pytest framework will independently conduct the affirmed tests. If any tests fail, pytest will also produce a detailed report on the issues discovered.  This will help ensure the robustness of the function and its adherence to the problem's requirements.  In order to fully visualize the execution of the tests, you may want to try using an IDE or test runner, which can provide a more detailed overview of the test outcomes, such as the execution time and any pertinent diagnostic information.