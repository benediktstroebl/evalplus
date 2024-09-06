```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    max_prime = 0
    for n, is_prime in enumerate(primes):
        if is_prime:
            max_prime = nums[n]
        elif max_prime % 10 != 0:
            max_prime = max(max_prime, nums[n])
    return sum(map(int, str(max_prime)))
```

The function `largest_prime_sum_of_digits` takes a list of integers (`nums`) as input and returns the sum of the digits of the largest prime number in the list.

The algorithm works as follows:
1. First, we initialize a list of boolean values (`primes`) where each value corresponds to whether the corresponding element in the input list is a prime number or not. All elements are initially assumed to be prime.
2. We then define a variable `max_prime` to keep track of the largest prime found so far. Initially, we set it to zero.
3. We iterate through each element of the input list, and for each element, we check if the corresponding boolean value in `primes` is still `True`. If it is, that means the current element is a prime number, and we update `max_prime` to be that value. 
 4. If the current element is not prime (i.e., `primes[n]` is `False`), we only update `max_prime` if the current number is larger than the current value of `max_prime` or if the current `max_prime` is not a multiple of 10. This is because we want to prioritize larger prime numbers and ensure that any non-prime numbers we consider are at least one digit long. 
5. Finally, we return the sum of the digits of the `max_prime` found. We convert the `max_prime` to a string and map each character to an integer to ensure that any numeric strings are converted properly.

This algorithm optimizes for speed by using the fact that all numbers in the list are initially considered as prime, and at each step, it only focuses on the largest prime found so far, gradually narrowing down the possible candidates for the maximum prime sum of digits.