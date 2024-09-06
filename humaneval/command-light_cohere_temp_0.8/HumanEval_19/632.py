```python
import pytest
from typing import List
def sort_numbers(numbers: str) -> str:
    assert numbers.isinstanceList List[
    unsorted list
    return ' '.join(sorted(numbers)))
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
# run tests
pytest. testing. can using -- pytest
 module is used to run tests. 
```  This Python script defines a function **`sort_numbers`** that takes a string of numbers as input and returns a sorted version of the numbers. The function uses the list data type to store the input numbers and uses the **`sorted`** function to sort the numbers in ascending order. The test function **`test_sort_numbers`** tests the **`sort_numbers`** function with a string containing the numbers **`three one five`**.  The **`pytest`** module is used to run the tests.   When execution, the script will display the test results and indicate whether the test passed or failed.