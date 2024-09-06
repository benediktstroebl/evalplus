```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if is_prime(x)]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```
The function `largest_prime_sum_of_digits(lst)` uses the filter function to create a list of prime integers from the input list `lst`. If the list of primes is empty, indicating no prime numbers in the list, the function returns 0. Otherwise, it finds the largest prime in the list of primes, converts it to a string, sums the digits of that string, and converts the sum back to an integer, and returns the result, ensuring correct functionality as described in the provided test cases.

The `is_prime(n)` function is also included to check whether an integer `n` is prime or not, which is a crucial step in solving the given problem. It efficiently checks for divisibility by any integer between 2 and the square root of the number `n`. 

To ensure the solution's functionality, it is important to include this prime checking function.