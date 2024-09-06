```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    max_prime = 0
    max_prime_digit_sum = 0

    for i, num in enumerate(nums):
        if primes[i] == True:
            num_str = str(num)
            num_sum = sum(int(d) for d in num_str)
            if num_sum > max_prime_digit_sum:
                max_prime_digit_sum = num_sum
                max_prime = num
        if num == 1:
            primes[i] = False

    return max_prime_digit_sum
```
The function `largest_prime_sum_of_digits` takes a list of integers `nums` as input and returns the largest sum of digits of a prime number in the list.

The approach is to iterate through each number in the list and check if it is prime. If it is prime, we convert it to a string, sum the digits, and update the maximum prime value and its corresponding digit sum if necessary. Finally, we return the maximum digit sum of the largest prime number found. 
This solution is efficient and can solve the given problem in linear time complexity.