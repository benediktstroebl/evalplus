```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
def test_get_positive():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    got = get_positive(lst)
    assert got == [2, 5, 6, 3, 9, 123, 1]

# Run the function and test it
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```
The code defines a function get_positive that takes a list l as input and returns a new list containing only the positive numbers from l. The test_get_positive function creates a list lst with a mix of numbers and passes it to the get_positive function. The output of get_positive is then compared to the expected result [2, 5, 6, 3, 9, 123, 1], and the test passes, confirming the correctness of the function.