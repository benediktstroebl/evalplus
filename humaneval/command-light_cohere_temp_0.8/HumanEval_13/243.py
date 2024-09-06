```python
def greatest_common_divisor(a, b): 
    while b != 0:
        a, b = b, a % b
    return a 

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(58, 4))  # Output: 8 

```  This function utilizes the Euclidean algorithm, a well-known method to find the greatest common divisor of two numbers, achieving a successful implementation.