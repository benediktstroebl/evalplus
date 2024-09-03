```python
def is_equal_to_sum_even(n):
    return n % 4 == 0 and sum(x % 2 for x in range(1, n + 1)) % 4 == 0
```
This function checks whether the given number n can be represented as the sum of exactly four positive even numbers. It does so by using a modular operator to check if n is divisible by 4, and using the "sum" function with an alternating summing mod 2 to check if the sum of odd numbers from 1 to n is also even.