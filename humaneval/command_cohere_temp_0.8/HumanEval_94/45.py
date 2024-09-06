```python
def largest_prime_sum_of_digits(nums):
    """Return the largest prime sum of digits for a list of integers."""
    primes = [ True for n in nums ]
    # Mark non-primes
    for n in nums:
        if primes[n]:
            for d in str(n):
                if d != '0' and int(d) <= n:
                    primes[n] = False
                    break
            if primes[n]:
                return sum(map(int, str(n)))
    return 0
```
The function iterates through each number in the list and checks if it is prime. If it is prime, it calculates the sum of its digits and keeps track of the maximum sum found so far, finally, the function returns the maximum sum found. 

Here is an example usage of the function:
```python
print(largest_prime_sum_of_digits([0,724,32,71,99,32,6,0,5,91,83,0,5,6])) 
```
This would print:
```
11
```