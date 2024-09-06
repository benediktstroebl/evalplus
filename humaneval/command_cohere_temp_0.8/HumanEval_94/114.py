```python
def largest_prime_sum_of_digits(nums):
    """Return the largest prime sum of digits for a list of integers."""
    primes = [True for n in nums]
    # Mark non-primes and calculate cumulative sum
    for n in range(2, int(np.sqrt(max(nums)) + 1)):
        if not primes[n]:
            continue
        for i in range(n, len(nums)):
            if nums[i] == n:
                primes[i] = False
                break
    # Calculate sum of digits of primes
    prime_sum = [sum(map(int, str(n))) for n in range(len(nums)) if primes[n]]
    return max(prime_sum)
```

The function `largest_prime_sum_of_digits` works by first iterating through the list of integers provided, assuming each value is prime initially. It then iterates through numbers from 2 to the square root of the largest number in the list, marking non-prime numbers as such. For each marked number, it goes through the list to find if it is present, and if so, it updates the corresponding entry to False and breaks out of the inner loop. Finally, it calculates the sum of digits for each prime number in the list, finds the maximum sum, and returns the result. 

This approach efficiently solves the problem by first identifying prime numbers and then calculating the sum of their digits. It ensures that the largest prime sum of digits is found and returned. 
```python
primes = [True for n in nums]
```
Here, I create a boolean list `primes` of the same length as the input list `nums`, initially marking each value in `nums` as prime. 

```python
for n in range(2, int(np.sqrt(max(nums)) + 1)):
    if not primes[n]:  # Check if n is not marked as non-prime
        continue
    for i in range(n, len(nums)):
        if nums[i] == n:  # If n is found in the list
            primes[i] = False
            break
```
In the nested loop, we first check if `n` is not marked as non-prime (`primes[n] == True`). If it is not marked, we skip to the next number. Otherwise, we iterate through the list, checking if `n` is present. If found, we mark it as non-prime (`primes[i] = False`) and break out of the inner loop. 

```python
prime_sum = [sum(map(int, str(n))) for n in range(len(nums)) if primes[n]]
```
Here, we create a list `prime_sum` containing the sum of digits for each prime number in the `primes` list. We iterate through the `primes` list and calculate the sum of digits for each prime number. 

```python
return max(prime_sum)
```
Finally, we return the maximum value from the `prime_sum` list, which represents the largest prime sum of digits among the numbers in the input list.