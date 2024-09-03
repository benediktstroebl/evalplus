```python
def below_threshold(lst, threshold):
    return all([x < threshold for x in lst])

# Test the function
# Passed test
assert below_threshold([1, 20, 4, 10], 5), "Function failed the test"
``` 
This script defines a function called `below_threshold` that takes in a list `lst` and a `threshold` value as input. It then uses the useful Python operator `all` to check if all elements in the list are less than the `threshold` value. The `assert` function is used to check the correctness of the function by passing in the function's output and expected value.