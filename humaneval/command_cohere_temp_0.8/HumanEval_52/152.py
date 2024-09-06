```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
The function `below_threshold` uses the built-in `all` function to iterate over each element in the list `l` and compares it with the threshold value `t`. It returns `True` if all elements in the list are below the threshold, and `False` otherwise.

Here is a simple test case to ensure the function is working as expected:
```python
def test_below_threshold():
    assert below_threshold([1, 2, 4, 10], 100) == True
    assert below_threshold([1, 20, 4, 10], 5) == False
``` 
The test case confirms that the function's behavior aligns with its definition, returning 'True' for the first example (where all numbers are less than the threshold), and 'False' for the second example.

To run these test cases, simply call the `test_below_threshold()` function with the Python interpreter, and it will validate the behavior of the `below_threshold` function.