```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x**0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` works by first filtering the list `lst` to retain only the prime numbers using the condition `x > 1 and all(x % n for n in range(3, int(x**0.5) + 1, 2))`. The int(`x**0.5`) part ensures that we're only checking up to the square root of x, which is an optimization so we don't waste computational effort checking large integers that aren't contributing to the prime checking.

Then it sums the digits for each prime number, converts the sum back to an integer, and finds the maximum value. The final result returned is the largest sum of digits among the prime numbers in the list. 

This approach ensures that the function solves the given problem in a concise and efficient manner. Let's break it down step by step. 

### Step 1: Finding Prime Numbers

The first step is to find the prime numbers in the list `lst`. This is done using a generator expression:
```python
primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x**0.5) + 1, 2)))]
```
Here's an explanation of the conditions used:
- `x > 1`: We're only interested in numbers greater than 1, as all numbers less than 2 are considered primes.
- `all(x % n for n in range(3, int(x**0.5) + 1, 2))`: This is the core of the Prime Number Theorem, which checks if `x` is a prime number. The range(3, int(x**0.5) + 1, 2) part ensures we only check divisors up to the square root of `x`, excluding fractions. This is a performance optimization.

###  Step 2: Sum of Digits for Each Prime

Once we have the list of prime numbers, the second step is to calculate the sum of the digits for each prime number. This is achieved by mapping the prime numbers to their digit sums using `map(int, str(x))`. The `map` function applies the `int` function to each character in the string representation of the prime number `x`, effectively summing the digits. This is done within the max function to find the maximum digit sum among the primes:
```python
return max(sum(map(int, str(x))) for x in primes)
``` 

Putting it all together, the function `largest_prime_sum_of_digits` solves the problem as stated, finding the largest prime number in the list and returning the sum of its digits. 

The function remains efficient given the optimizations in prime checking, and the whole solution is self-contained within the function, making it easy to reuse and test.