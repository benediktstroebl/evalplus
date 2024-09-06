```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    # Ensure positive values
    a = abs(a)
    b = abs(b)

    #Prime factors and divisors
    factors_of_a = [i for i in range(2, int(a**0.5) + 1) if a % i == 0]
    factors_of_b = [i for i in range(2, int(b**0.5) + 1) if a % i == 0]

    #Find the greatest common divisor
    common_divisor = 1
    for factor_a in factors_of_a:
        for factor_b in factors_of_b:
            if factor_a == factor_b:
                continue
            common_divisor = common_divisor * factor_a

    return common_divisor
``` 
This function takes two integers a and b as input and returns the greatest common divisor of a and b.

It first checks if either a or b is not defined, and returns 0 in such cases. Then it converts both a numbers to positive using the **abs()** function to avoid negative numbers. It then finds thees prime factors of both numbers and stores them in lists, factors_of_a and factors_of_b. Finally, it iterates through the prime factors of both numbers and finds the highest number among them that appears in both lists.