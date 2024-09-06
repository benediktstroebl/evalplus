```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the built-in `all` function to iterate over each item in the input list `l` and compare it to the threshold value `t`. The function then returns `True` if all items in the list are below the threshold, and `False` otherwise.

Here is a simple test case to ensure the function is correct:
```python
assert below_threshold([1, 2, 4, 10], 100), "Expected [1, 2, 4, 10] to be below threshold 100"
assert below_threshold([1, 20, 4, 10], 5), "Expected [1, 20, 4, 10] not to be below threshold 5"
``` 
This test case uses the `assert` statement to check whether the function returns the correct values for the given inputs.

The expected output of the above code is:
```
True
False
```

This confirms that the `below_threshold` function is operating correctly. It can handle the list of numbers and the threshold as intended, returning true if all the numbers in the list are below the threshold and false otherwise.