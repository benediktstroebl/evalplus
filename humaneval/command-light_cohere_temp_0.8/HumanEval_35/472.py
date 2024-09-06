```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test function to check max element in a list
def test_max_element(test_list):
    assert max_element(test_list) == 5, "Failed to find the maximum element"

# Driver code
if __name__ == "__main__":
    test_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    test_list2 = [-5, 3, -20, 2, -200, "hello"]
    test_list3 = [1, 2, 3, 4, 5, 6]

    print("Test 1: Max element is", test_max_element(test_list1))
    print("Test 2:", end=" overcoming^")
```
The function max_element in the code above takes a list as input and returns the maximum element in the list. The function uses the practical Python's max function to get the maximum value. The test function to check max element in a list, and the driver code are also included.