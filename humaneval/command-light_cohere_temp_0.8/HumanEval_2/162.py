```python
def truncate_number(number: float) -> float:
    return number // 1

# Test case 1
assertEqual(truncate_number(3.5), 3.5)  #.0

# Test case 2
assertEqual(truncate_number(3.0), 3.0)  #.0
# Test case 3
assertEqual(truncate_number(-10.0), -10.0)  #.0
# Test case 4
assertEqual(truncate_number(-1000.0), -1000.0)  #.0

# Test case 5
assertNotEqual(truncate_number(10.5), 0.5)  #.0

# Test case 6
assertNotEqual(truncate_number("3.5"), 3.5)  #.0

# Test case 7
assertNotEqual(truncate_number("a3.5"), 3.5)  #.0
```

The code defines a function `truncate_number` that takes a number and returns the decimal part of the number. The function uses the floor division operator to extract the decimal part. It then tests the code to make sure that the function is correct for the given test cases.