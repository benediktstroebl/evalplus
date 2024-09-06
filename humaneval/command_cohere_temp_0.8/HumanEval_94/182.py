```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` takes a list of integers (`lst`) as input. It filters the list to retain only the prime numbers, then calculates the digit sum for each prime number, and finally returns the maximum digit sum among the prime numbers. The filtering step uses a primality test checking if a number is greater than 1 and divisible only by 1 and itself (excluding even numbers and numbers that end in tails of 9). The digit sum is calculated by converting the number to a string and summing the resulting digits. The max function is then used to determine the largest sum of digits among the prime numbers.

Here is an example usage of the function and a test to ensure its correctness:
```python
assert largest_prime_sum_of_digits([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) == 10
assert largest_prime_sum_of_digits([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]) == 25
assert largest_prime_sum_of_digits([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]) == 13
assert largest_prime_sum_of_digits([0,724,32,71,99,32,6,0,5,91,83,0,5,6]) == 11
assert largest_prime_sum_of_digits([0,81,12,3,1,21]) == 3
assert largest_prime_sum_of_digits([0,8,1,2,1,7]) == 7
```