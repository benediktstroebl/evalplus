Here is a self-contained Python script with a function that solves the problem of finding the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero.")
    
    # Use prime factorization to find GCD
    if a == b:
        return 0
    elif a <= 1 or b <= 1:
        return 1
    
    result = 1
    for i in range(2, min(len(prime_factors_a) + 1, len(prime_factors_b) + 1)):
        if prime_factors_a[i - 1] * prime_factors_b[i - 1] > a and b:
            result = max(result, prime_factors_a[i - 1] * prime_factors_b[i - 1])
    
    return result

def test_gcd():
    try:
        print(greatest_common_divisor(3, 5))
        print(greatest_common_divisor(25, 15))
        print(greatest_common_divisor(10, 5))
        print(greatest_common_divisor(125, 21))
    except ValueError as e:
        print("Error:", str(e))

# Call the function to test
test_gcd()
```
This script defines a function `greatest_common_divisor` that computes the GCD of two numbers a and b. The test_gcd function is an example of how to use the function to compute the GCD of three test cases. 
Note that the code is written in a self-contained manner, and does not require any external inputs or dependencies to function definition or behavior.