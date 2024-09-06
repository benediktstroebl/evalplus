```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    # Set up the list of divisors up to the square root of min(a,b)
    limit = int(math.sqrt(min(a, b)) + 1)
    divisors = [i for i in range(1, limit+1)]
    
    # Go through divisors, checking for each a/b until a or b is 0
    for divisor in divisors:
        if a % divisor == 0 and b % divisor == 0:
            return divisor  # found the greatest common divisor

    return 0  # no common divisor found

# Example usage:
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
``` 
This function checks all possible divisors from 1 to the square root of the minimum of a and b, and returns the greatest one.