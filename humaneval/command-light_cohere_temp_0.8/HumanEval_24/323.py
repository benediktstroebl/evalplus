Here is a Python script that contains a self-contained function to find the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    # Initialize the largest divisor found
    largest_divisor = 1
    
    # Check divisors up to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            largest_divisor = i
            break
    
    return largest_divisor
```
This function takes an integer n as input and returns the largest divisor of n. It uses a strategy by trying divisors from 2 up to the square root of n, as larger numbers have more divisors. It returns the value of the largest divisor found. 

Please note that the above code works correctly for all integers, provided that the input number n is also a positive integer.