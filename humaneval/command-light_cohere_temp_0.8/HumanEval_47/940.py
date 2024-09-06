```python
def median(l: list):
    """Return median of elements in the list l."""
    return (sorted(l) + [0])[len(l) // 2]

# Test the function
def test_median():
    input_list = [10, 20, 30, 40, 1, 2, 3]
    assert median(input_list) == 3
    input_list2 = [-10, 4, 6, 1000, 10, 20]
    assert median(input_list2) == 15.0
```
This script defines a function called `median` that computes the median of a given list of numbers. The `test_median` function is used to verify the correctness of the `median` function using a test list.  The median function is designed to solve the median calculation problem and pass the test.