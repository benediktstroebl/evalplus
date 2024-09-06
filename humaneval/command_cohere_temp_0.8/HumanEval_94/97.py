```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    max_prime = 0
    for n, is_prime in enumerate(primes):
        if is_prime:
            max_prime = nums[n]
        elif max_prime > nums[n]:
            max_prime = nums[n]
    return sum(map(int, str(max_prime)))
```

The function `largest_prime_sum_of_digits` uses an array of boolean values (`primes`) to determine prime status for each number in the input list. It initializes `max_prime` to the first element of the list and subsequently compares it with the boolean indicator of primality for each element. If an element is prime, `max_prime` is updated to its value; otherwise, if the max_prime is greater than the current element, it is updated to the current element's value. This ensures that `max_prime` is the largest prime in the list. The function then converts the `max_prime` value to a string and sums its digits to give the final result.