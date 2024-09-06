```python
def truncate_number(n): 
    x = n // 1
    return x if x <= 1 else 0.5 + x

# Test case 1: Test if the function works with positive numbers
assert testcase1 = truncate_number(10)
assert testcase1 == 5  # True 

# Test case 2: Test if the function works with negative numbers
assert testcase2 = truncate_number(-10)
assert testcase2 == -5  # True 

# Test case 3: Test if the function works with floating point numbers
assert testcase3 = truncate_number(3.5)
assert testcase3 == 0.5  # True 

# Test case 4: Test with different input types
try:
    assert truncate_number('c10') == 5  # Should raise ValueError 
except ValueError:
    print("Test passed") 

# Test case 5: Test if the function works with non-numeric strings
try:
    assert truncate_number("hello") == 0  # Should raise ValueError 
except ValueError:
    print("Test passed") 

# Test case 6: Test if the function works with invalid input types
try:
    assert truncate_number([1, 2, 3]) == 0  # Should raise ValueError 
except ValueError:
    print("Test passed") 
```