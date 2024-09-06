Here's the self-contained Python function that finds the largest divisor of a given number n: 

```python
def largest_divisor(n: int) -> int:
    # Initialize the largest divisor found so far
    largest_divisor = n
    divisor = n

    while divisor <= n:
        # Calculate the smallest odd divisor of n
        i = 4 * (n - 1) // 3
        while i <= n:
            if n % i == 0:
                divisor = i
                break
        i += 4

    # Return the largest divisor found
    return largest_divisor
``` 
The function uses the method of trial and error to find the largest divisor. It iterates through numbers from 1 to n, and checks if they are divisors of n. The numbers are generated using the formula 4 * (n-1) / 3 are the smallest odd divisors of n.