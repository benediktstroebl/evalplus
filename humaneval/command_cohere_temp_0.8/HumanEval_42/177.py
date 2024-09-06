Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a new list with its elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. The return value is a new list with the incremented elements. 
The script also includes test cases to verify the function's behavior against the given problem statement. Place these tests in a separate file called `test_incr_list.py` to verify the function's correctness:
```python
import incr_list

def test_incr_list():
    assert incr_list.incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list.incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
``` 
Place the function code from the first cell into a module named `incr_list.py` and ensure you run the tests with the command `python -m pytest test_incr_list` in your terminal to verify the function's correctness against these test cases. 
This way, you have a self-contained Python script that defines the `incr_list` function and includes tests to validate its behavior against the provided problem statement.