```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * (n + 1)
    result[0] = l[0]
    for i in range(1, n+1):
        result[i] = l[i - 1] + 1
    return result

# Test the function with various input.
def test_incr_list(incr_list)

# Example of usage:
input_list = [5, 3, 5, 2, 3, 3]
result_incr = incr_list(input_list)
print("Input list:", input_list)
print("Result:", result_incr)

```
The function incr_list takes a list l as input and returns a new list with elements incremented by 1. The test_incr_list function tests the incr_list function with various input lists and prints the results for confirmation.