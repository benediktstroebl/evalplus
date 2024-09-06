```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
test_incr_list = [
    [
        ("Input: [5, 3, 5, 2, 3, 3, 9, 0, 123]").format('#'),
        (result = incr_list([5, 3, 5, 2, 3, 3, 3, 9, 0, 123])).format('#'),
        ("Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124"]).format('#')
    ]

if __name__ == "__main__":
    test_incr_list
```
This code defines a function `incr_list` that simply increments each element in the input list by 1 and returns the updated list. It also includes a test cases to ensure the function works correctly for various inputs.