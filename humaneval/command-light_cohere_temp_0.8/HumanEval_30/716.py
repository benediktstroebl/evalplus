```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with various input lists 

def test_get_positive():
    tests = [
        [-1, 2, -4, 5, 6],
        [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
        [5, 0, -8, -6, -4, -2, -3],
        [123, -9, 7, -8, 3, -5, 5, -1]
    ]

    for test_list in tests:
        got = get_positive(test_list)
        expected = test_list
        print(f"Test 1: Got: {got}, Expected: {expected}")
        assert got == expected, "Test 1 failed" 

# Test 2: None input
test_get_positive([])
print("Test 2: Got: [], Expected: []")
assert get_positive([]) == [], "Test 2 failed" 

# Test 3: List with all negative numbers
test_get_positive([-1, -2, -3, -4, -5])
print("Test 3: Got: [-1, -2, -3, -4, -5], Expected: []")
assert get_positive([-1, -2, -3, -4, -5]) == [], "Test 3 failed" 
```
This code defines a function called `get_positive` that takes an input list and returns a new list containing only the positive elements from the original list. The `test_get_positive` function contains various tests for the `get_positive` function, including tests with different list inputs and empty lists. 
The code also includes a test case with a list containing only negative numbers, which should produce an empty list as the expected output.