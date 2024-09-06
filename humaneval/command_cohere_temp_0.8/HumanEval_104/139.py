```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This Python script defines a function `unique_digits` that takes a list of positive integers as input (`xs`). It filters this list and returns a sorted list of all elements that do not contain any even digits. This is done using a list comprehension that checks each digit in the string representation of an integer (`str(x)`), and if any digit is even (`int(y) % 2 == 0`), it will not be included in the resulting list. The `sorted` function ensures that the returned list is ordered in ascending fashion. 

To showcase the function, I've added a test module (`test_unique_digits.py`) that contains test cases to validate the behavior of the function. Using Python's built-in `unittest` framework, the script verifies that the output of `unique_digits` matches the expected output for each case. 

This way, the provided solution is self-contained and can be executed and tested directly by dropping it into a Python environment.