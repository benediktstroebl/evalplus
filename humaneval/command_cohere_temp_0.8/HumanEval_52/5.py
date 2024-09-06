```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and quickly checks if all elements are below the threshold `t`. 

Here is a usage example with a test to ensure the function behaves as intended:
```python
assert below_threshold([1, 2, 4, 10], 100), "Expected True"
assert not below_threshold([1, 20, 4, 10], 5), "Expected False"
```
This test case validates the behavior of the `below_threshold` function against the expected True and False results.