```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compares each element with the threshold value `t`.  If all elements are less than `t`, the function returns `True`, otherwise `False`.

Here is a test case to ensure the function above works properly:
```python
def test_below_threshold():
    # True case
    assert below_threshold([1, 2, 4, 10], 100) == True

    # False case
    assert below_threshold([1, 20, 4, 10], 5) == False

test_below_threshold()
```
This test case provides two examples; one for which the function returns true and one for which the function returns false. The `assert` statements will ensure that our function behaves as expected.  The final line of the test case calls the function with different input parameters to test its functionality.  It is imperative to have test cases that cover different scenarios to ensure that the function behaves correctly for all cases.  This helps ensure that the code is fit for purpose.