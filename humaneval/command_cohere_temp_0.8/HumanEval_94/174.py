```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x >= 2 and all(x % d for d in range(3, int(x**0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` takes a list of integers (`lst`) as input. It uses a list comprehension to filter out prime numbers from the list, then maximizes the sum of digits for the largest prime number found using the max function and string summing. 

The function returns the largest prime value sum of digits. You can call this function with a list of integers as argument to see the result. 

For example:
```python
print(largest_prime_sum_of_digits([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]))
```

The output will be:
```
10
```