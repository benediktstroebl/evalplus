```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
def test():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

if __name__ == "__main__":
    # Main function
    test()
``` 
This script defines a function max_element that takes a list l as input and returns the maximum element in the list. The function uses the approach with the built-in function max() from the Python standard library. 

The test function has test cases that pass the corresponding function tests. The main function is used to execute the test function, which contains test cases to verify the correctness of the max_element function.