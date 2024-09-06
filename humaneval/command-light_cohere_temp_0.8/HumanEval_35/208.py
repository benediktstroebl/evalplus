```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function to pass test cases
def test():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123

if __name__ == "__main__":
    test()
``` 
This code defines a function max_element that calculates the maximum element in a list. The function uses the test assertion library's max function to find the maximum element. It also includes a test function that creates a test list and asserts the output of the max_element function for the given test list, which ensures the correctness of the max_element function.