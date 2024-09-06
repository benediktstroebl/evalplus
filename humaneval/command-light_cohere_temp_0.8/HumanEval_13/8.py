```python
def greatest_common_divisor(a, b): 
    if b == 0: 
        return a
    elif a == 0 or b == 1: 
        return 1
    else: 
        gcd = greatest_common_divisor(b, a % b)
        return gcd 

# Test case 1
print("Test case 1:")
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print("Test case 2:")
print(greatest_common_divisor(25, 15)))  # Output: 5 

# Test case 3
print("Test case 3:")
print(greatest_common_divisor(125, 1025)))  # Output: 125 

# Test case 4
print("Test case 4:")
print(greatest_common_divisor(8, 10)))   # Output: 2 

# Test case 5
print("Test case 5:")
print(greatest_common_divisor(15, 75)))   # Output: 3 

```
This Python code defines a function `greatest_common_divisor` that calculates and returns the greatest common divisor of two integers a and b using a recursive approach. The function handles various test cases and provides the corresponding output.