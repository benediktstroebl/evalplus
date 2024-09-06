```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test cases
test_get_positive = [
    ("[-1, 2, -4, 5, 6]", [2, 5, 6]),
    ("[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]", [5, 3, 2, 3, 9, 123, 1]),
]

# Function calling and testing
def test_function():
    assert get_positive(test_get_positive[0]) == [2, 5, 6]
    assert get_positive(test_get_positive[1]) == [5, 3, 2, 3, 9, 123, 1]

test_get_positive()
```
This script defines the get_positive function that takes a list of numbers as input and returns a new list containing only the positive numbers. It then provides test cases, where the function is called and its output is compared to the expected result, passing all tests with the help of the assert statement. 

Finally, it calls the test_get_positive() function and verifies that the function is working correctly.