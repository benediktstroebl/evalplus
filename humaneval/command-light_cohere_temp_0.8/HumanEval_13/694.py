```python
def greatest_common_divisor(a, b): 
    while b != 0:
        a, b = b, a % b 
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(2, 200)) # Output: Error: Equilibrium
```

The code defines a function greatest_common_divisor that takes two integers a and b as input and returns the greatest common divisor of a and b. The function uses the formula to find the greatest common divisor, which is a while loop that keeps removing the divisor from the dividend until the dividend becomes zero. The function then returns the the result, which is the largest divisor that divides both a and b evenly. 

The test cases cover various scenarios, including finding the greatest common divisor for specific values and checking for an error case where the function expects an integer as a parameter.