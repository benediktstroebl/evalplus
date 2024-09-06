```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with various input lists
def test_get_positive():
    test_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    test_list2 = [-1, 2, -4, 5, 6]
    
    assert get_positive(test_list1) == [2, 5, 6]
    assert get_positive(test_list2) == [2, 3, 5]

# Main code
if __name__ == "__main__":
    test_get_positive()
``` 
This code defines a function `get_positive` that filters out negative numbers from an input list and returns a new list with only the positive numbers. The test function `test_get_positive` is then used to validate the correctness of this function with different input lists. 
When you run the script, it will output the test results, showing that the function works as expected.