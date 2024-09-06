```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function
tests = [
    [1, 2, 3],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

for test in tests:
    print(max_element(test))  # Output: 123
``` 
This Python code defines a function max_element that aims to find the maximum element in a given list. The function achieves this goal by utilizing the max() function, which returns the maximum value of the provided list. The test cases are an list of lists, and each test ensures that the max_element function can correctly identify the maximum element within the list.