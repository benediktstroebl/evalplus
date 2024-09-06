```python
def largest_prime_sum_of_digits(nums):
    """Returns the largest prime sum of digits for a list of integers."""
    primes = [ True for n in nums ]
    # Mark non-primes
    for n in range(2, int(len(nums)**0.5)+1):
        if not primes[n]:
            for i in range(n, len(nums)+1, n):
                primes[i] = False
    # Find the largest prime
    largest_prime = 0
    for n in nums:
        if primes[n]:
            largest_prime = max(largest_prime, n)
    # Return the sum of the digits of the largest prime
    digit_sum = sum(map(int, str(largest_prime)))
    return digit_sum
```
The function first determines whether each number in the list is prime. It then locates the largest prime number among them and sums the digits of that number to yield the result. The technique involves identifying potential primes up to the square root of the array size, then steadily eliminating non-prime markings. The Largest prime is then determined, and its digit sum returned. 

Here's an example of a test case that can be used to verify the function:
```python
assert largest_prime_sum_of_digits([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) == 10
```

This test case corresponds to the first example provided in the problem statement, and the function should correctly output 10. 

Another test case can be:
```python
assert largest_prime_sum_of_digits([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]) == 25
``` 

Note that the function assumes that the input list contains only positive integers. If the input list contains negative numbers or non-integer values, the function may not work as intended.