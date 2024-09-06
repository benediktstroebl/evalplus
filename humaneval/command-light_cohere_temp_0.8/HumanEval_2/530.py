```python
def truncate_number(number: float) -> float:
    # Positive floating point number
    # 1.Get the integer part
   
    decimal = number - floor(number)
    # Return the decimal part of the number
    return decimal

# Test cases
# Test 1: 
assertEqual(truncate_number(3.5), 0.5)
# Test 2: 
assertEqual(truncate_number(-3.5), 0.5)
# Test 3: 
assertEqual(truncate_number(-0.5), 0.5)
# Test 4: 
assertEqual(truncate_number(0.5), 0.5)
# Test 5: 
assertEqual(truncate_number(0.0), 0.5)
# Test 6: 
assertEqual(truncate_number(0.1), 0.0)
# Test 7: 
assertEqual(truncate_number(0.5000000001),
```