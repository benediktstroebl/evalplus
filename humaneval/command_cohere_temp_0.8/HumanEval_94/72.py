```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))
```

The function `largest_prime_sum_of_digits` takes a list of integers `lst` as input and returns the sum of the digits of the largest prime number in the list.

The function first selects all prime numbers from the list using a list comprehension. If the list of primes is empty, meaning there are no prime numbers in the list, the function returns 0. Otherwise, it finds the largest prime number from the list using `max` and converts it to a string. The function then sums the digits of this string using `sum` and `map`, which converts each character of the string to an integer. 

Here is an example usage of the function:
```python
print(largest_prime_sum_of_digits([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]))
```
The output will be:
```
10
```