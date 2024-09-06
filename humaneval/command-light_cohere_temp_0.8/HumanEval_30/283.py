```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test cases
test_get_positive = [
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6], "Passing test 1"
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1], "Passing test 2"
]

# Main code
if __name__ == "__main__":
    test_get_positive

``` 
This script defines a function called `get_positive`, which takes a list as an argument and returns a new list containing only the positive numbers from the input list. The function uses a Python list comprehension and boolean logic to filter out the positive numbers from the input list.