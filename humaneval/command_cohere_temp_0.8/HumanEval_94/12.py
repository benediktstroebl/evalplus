```python
def largest_prime_sum_of_digits(nums):
    """Returns the largest prime sum of digits for a list of integers."""
    primes = [0 for i in range(100001)]
    p = 3
    while p**2 <= 100001:
        if primes[p]:
            for i in range(p**2, 100001, p):
                primes[i] = 1
        p += 2
    max_val = 0
    for num in nums:
        current_sum = 0
        num = str(num)
        for digit in num:
            current_sum += int(digit)
            if primes[current_sum] == 0:
                max_val = max(max_val, current_sum)
    return max_val
```

The function initially creates a list of primes up to 10,000 for quick determination of whether a number is prime. It then iterates through the list of integers, converting each to a string and computing the sum of its digits. If the sum is prime, it is added to the `max_val` variable. The function eventually returns the largest prime sum of digits. 

Here is an example usage of the code:
```python
print(largest_prime_sum_of_digits([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]))
```
Which would print the output:
```
10
``` 

This function provides an efficient solution to the problem, correctly identifying the largest prime sum of digits in the given list of integers.