```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    max_prime = 0
    max_prime_digit_sum = 0
    
    for n, is_prime in enumerate(primes):
        if is_prime:
            prime_digits = [int(d) for d in str(nums[n]) if d.isdigit()]
            prime_digit_sum = sum(prime_digits)
            if prime_digit_sum > max_prime_digit_sum:
                max_prime_digit_sum = prime_digit_sum
                max_prime = nums[n]
        
    return max_prime_digit_sum
```
The function `largest_prime_sum_of_digits` takes a list of integers `nums` as input and returns the sum of the digits of the largest prime number in the list.

The algorithm proceeds as follows:
1. Initialize a boolean list `primes` to be true for each element in the input list. This pre-assuming each number to be prime.
2. Initialize two variables `max_prime` and `max_prime_digit_sum` to keep track of the largest prime number and the sum of its digits.
3. Loop through each element in the list:
    1. If the number is prime: 
        - Convert the number to a string and extract its digits.
        - Sum the digits and compare this sum with the current largest sum of prime digits.
        - Update the `max_prime_digit_sum` and the prime that achieves this if the sum is larger.
4. Finally, return the `max_prime_digit_sum` which corresponds to the required output. 

This algorithm has a time complexity of `O(n`), where n is the number of elements in the input list, as it iterates through each element once.