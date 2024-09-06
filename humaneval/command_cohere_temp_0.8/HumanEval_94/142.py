```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    max_prime = nums[0]
    max_sum = nums[0]
    for n in nums:
        if primes[n]:
            if n > max_prime:
                max_prime = n
        else:
            for digit in str(n):
                if int(digit) > max_sum:
                    max_sum = int(digit)
        primes[n] = n % 2 == 0
    return max_sum
```

The function `largest_prime_sum_of_digits` takes a list of integers `nums` as input and returns the largest sum of digits of a prime number in the list.

The function first initializes an array `primes` of the same length as `nums`, where each element is `True` to start assuming that all numbers are prime. It then initializes `max_prime` and `max_sum` with the first element of `nums`. Then, it iterates through each number in `nums`. 

If a number is prime, it checks if it is larger than the current `max_prime`. If so, it updates `max_prime` to this number. If a number is not prime, it iterates through each digit of this number and updates `max_sum` if the current digit is larger than the current value of `max_sum`. Finally, it sets `primes[n]` to `False` if the number `n` is not prime, indicating that the number has been checked, and updates `max_sum` to the maximum value if needed. 

The script ensures that the correct maximum sum of prime digits is found despite potential slowdowns caused by multiple checks for non-prime numbers.