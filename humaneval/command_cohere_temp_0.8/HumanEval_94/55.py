```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if is_prime(x)]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The function `largest_prime_sum_of_digits(lst)` uses a list comprehension to filter the input list `lst` and create a new list `primes` that includes only prime numbers. The function then finds the largest number in the `primes` list, converts it to a string, and sums the digits of that string. If the list of primes is empty, the function returns 0. 

The `is_prime(n)` function checks whether a given number n is prime or not. It starts by handling the edge case where n is less than 2, returning False immediately. Then, it iterates through the numbers from 2 to the square root of n, checking for divisibility. If n is divisible by any of these numbers, it returns False. If it reaches the end of the loop without finding a divisor, it returns True, indicating that n is prime. 

Here's an example usage of the function:
```python
largest_prime_sum_of_digits([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3])
```
Which should return the output:
```
10
```