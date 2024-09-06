```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t` using the `<` operator. The `all()` function returns `True` if all comparisons are `True`, indicating that all elements are below the threshold, otherwise `False`. 
The function's docstring demonstrates its behavior on example inputs.
```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
```python
# Test suite
def test_below_threshold():
    assert below_threshold([1, 2, 4, 10], 100) == True
    assert below_threshold([1, 20, 4, 10], 5) == False
```
To run the test, you can copy and paste the code into a Python interpreter or save it in a file with a `.py` extension and run it using the `python file_name.py` command.

This approach uses a concise one-liner to achieve the desired functionality and includes a self-contained test case to validate its behavior.