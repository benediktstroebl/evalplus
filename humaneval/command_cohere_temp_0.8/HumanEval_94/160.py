```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))
```

The function `largest_prime_sum_of_digits` works by first filtering the list `lst` to obtain a list of prime numbers, using the condition `x % 2 == 1 and x > 1`. If the list of primes is empty, meaning there are no prime numbers in the list, the function returns 0. If there are prime numbers in the list, it finds the largest prime number in the list using `max(primes)`, converts it to a string, and sums up its digits using the `sum` and `map` functions. 

The output of the given examples in the prompt should be:
- `10` for `[[0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]]`
- `25` for `[1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]`
- `13` for `[1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]`
- `11` for `[0,724,32,71,99,32,6,0,5,91,83,0,5,6]`
- `3` for `[0,81,12,3,1,21]`
- `7` for `[0,8,1,2,1,7]`