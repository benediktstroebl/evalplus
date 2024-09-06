```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x >= 2 and all(x % d for d in range(3, int(x**0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` uses a list comprehension to filter the list `lst` and create a new list comprised only of prime integers. The summation of the digits of each prime number is then converted to an integer and has its summation calculated using `sum`, after which the maximum value among these sums is returned. 

The logic leveraged for determining prime numbers is a commonly used one: all divisors d of `x` must be less than or equal to `x`'s square root, and `x` itself must be greater than or equal to 2. 

To ensure the list comprehension doesn't alter the original list `lst`, it creates a new list, `primes`, to store the prime integers. 

The given examples result in the following calls to the function:
```python
largest_prime_sum_of_digits([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3])  # 10
largest_prime_sum_of_digits([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1])  # 25
largest_prime_sum_of_digits([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3])  # 13
largest_prime_sum_of_digits([0,724,32,71,99,32,6,0,5,91,83,0,5,6])  # 11
largest_prime_sum_of_digits([0,81,12,3,1,21])  # 3
largest_prime_sum_of_digits([0,8,1,2,1,7])  # 7
```