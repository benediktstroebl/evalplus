```python
def greatest_common_divisor(a, b): 
    if b == 0: 
        return a 
    return greatest_common_divisor(b, a % b) 

# Test cases
assertEqual(greatest_common_divisor(3, 5), 1)

assertEqual(greatest_common_divisor(25, 15), 5)

# Without modulo
assertEqual(greatest_common_divisor(19, 41), 7)

# Edge case
assertEqual(greatest_common_divisor(0, 4), 4)
```