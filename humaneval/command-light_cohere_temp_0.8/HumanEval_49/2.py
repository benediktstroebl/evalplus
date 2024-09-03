```python
def modp(n, p):
    return (pow(2, n, p) % p)

# Test case 1: power(2) modulo 5
assert modp(3, 5) == 3

# Test case 2: power(1101) modulo 101
assert modp(1101, 101) == 2

# Test case 3: power(0) modulo 101
assert modp(0, 101) == 1

# Test case 4: power(3) modulo 11
assert modp(3, 11) == 8 

# Print your results
print("Test Case 1 Passed!")
print("Test Case 2 Passed!")
print("Test Case 3 Passed!")
print("Test Case 4 Passed!")
``` 

The provided Python script defines a function `modp` that calculates the result of raising a number to the power of n, then taking the modulus of that result with respect to the given prime number p. The script then conducts several tests on this function, ensuring its correctness. 

The tests pass successfully, and the function is verified to produce the correct results for the given inputs.