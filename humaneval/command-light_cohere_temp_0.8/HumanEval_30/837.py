```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

#Test the function with sample inputs
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

#Assert that the output of the get_positive function matches the expected list
def test():
    assert test_get_positive == get_positive(test_get_positive)

#Main program
test()
```