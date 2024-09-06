```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the built-in `all` function to iterate over each item in the input list `l` and compare it to the threshold value `t`. It then returns `True` if all items in the list are below the threshold, and `False` otherwise.

Here is a simple test case to ensure the function is working as intended:
```python
def test_below_threshold():
    assert below_threshold([1, 2, 4, 10], 100) == True
    assert below_threshold([1, 20, 4, 10], 5) == False
``` 
This test case demonstrates two specific use-cases of the function, and the assertions correspondingly check that the function returns the expected boolean values for these use-cases.  This way, you can guarantee the function behaves as expected and is correctly solving the problem.