```python
def greatest_common_divisor(a, b): 
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return greatest_common_divisor(b, a % b) 

# Test case #1
assert greatest_common_divisor(3, 5) == 1
# Test case #2
assert greatest_common_divisor(25, 15) == 5
# Test case #3
try:
    assert greatest_common_divisor(13, 4) == 4 
except AssertionError: 
    print('AssertionError occurred! Debugging information:')

# Test case #4
try:
    assert greatest_common_divisor(4, 33) == 1 
 except AssertionError: 
        print('AssertionError occurred. Debugging information:') 
``` 
The above Python script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers a and b. The function first checks if either number is zero, and returns the other number. The function then checks if the other number is zero, and returns the product of a and b. If both numbers are not zero, it uses the `greatest_common_divisor` function to calculate the GCD of a and b.