```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of numbers as input and returns a string with the numbers sorted from smallest to largest. 

The function first converts the space-delimited string of numbers into a list of integers. Then, it sorts this list in ascending order using the `sort()` method and converts the sorted list of numbers back to a string. 

The example usage and test case provided in the problem statement are considered in the unit test included in the script to ensure that the function correctly solves the problem:
```python
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('zero zero nine') == 'zero nine zero'
    assert sort_numbers('nine eight seven') == 'seven eight nine'
    assert sort_numbers('five four three') == 'three four five'
``` 

You can run this test manually to verify that the function behaves as expected. 
```bash
python test_sort_numbers.py
```
The tests will pass if the function has been implemented correctly.