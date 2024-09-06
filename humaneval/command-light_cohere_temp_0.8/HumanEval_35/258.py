```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test cases
def test():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Main program
if __name__ == "__main__":
    test()
```
This script defines a function max_element that takes a list as input and returns the maximum element in the list. The function also has test cases to ensure its correctness. The final step is to run the test function to verify the expected results.