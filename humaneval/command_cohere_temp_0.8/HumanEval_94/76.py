```python
def largest_prime_sum_of_digits(nums):
    primes = [i for i in nums if is_prime(i)]
    return max(sum(map(int, str(p))) for p in primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The function `largest_prime_sum_of_digits(nums)` uses the `is_prime()` helper function to generate a list of prime integers from the input list. Then it finds the maximum sum of digits among these prime numbers. The `is_prime()` function checks if a number is divisible by any number from 2 to the square root of the number, if not, then it's a prime number. 

This solution passes all the test cases mentioned in the prompt. 

```python
# Tests
assert largest_prime_sum_of_digits([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) == 10
assert largest_prime_sum_of_digits([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]) == 25
assert largest_prime_sum_of_digits([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]) == 13
assert largest_prime_sum_of_digits([0,724,32,71,99,32,6,0,5,91,83,0,5,6]) == 11
assert largest_prime_sum_of_digits([0,81,12,3,1,21]) == 3
assert largest_prime_sum_of_digits([0,8,1,2,1,7]) == 7
```