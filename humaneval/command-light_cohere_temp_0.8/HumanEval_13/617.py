```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    elif a == 1:
        return b
    else:
        # Compute gcd(a, b) using the extended Euclidean algorithm
        g, b = divmod(a, b)
        return g + greatest_common_divisor(b, a)
    return_value = greatest_common_divisor(3, 5)
    print(f'The GCD of {3} and {5} is {return_value}')
    return_value = greatest_common_divisor(25, 15)
    print(f'The GCD of {25} and {15} is {return_value}')
```
This code defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers a and b. It uses the calculating gcd using the extended Euclidean algorithm, which is a more efficient method for finding the gcd. The code then provides test cases for the function, passing the values 3 and 5 and 25 and 15 respectively. It prints the expected output, which are the GCD values for the respective test cases.