```python
def unique(l: list):
    return sorted(set(l))

# Test the function with a sample input and check the expected output
assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])
```  This code defines a function unique that takes a list as input and returns a new list containing unique elements from the original list, which are sorted in ascending order. The test at the made to ensure that the function produces the correct output when applied to the test input.