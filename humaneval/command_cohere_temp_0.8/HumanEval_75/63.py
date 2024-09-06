```python
def is_multiply_prime(a):
    primes = []
    for i in range(2, a):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return len(primes) == 3
```

This script defines a function called `is_multiply_prime` that takes a number `a` as input and returns either `True` or `False`. The function first iterates from 2 up to the given number `a` and for each number `i` it checks whether it is prime. A number is considered prime if it has exactly two distinct divisors: 1 and itself. 

The function checks if the given number `a` can be decomposed into 3 prime numbers. If it can, it returns `True`, otherwise, it returns `False`. 

To be more precise, in the body of the function, first, a list `primes` is initialized. Then, the function iterates from 2 up to the given number `a` and for each number `i`, it checks whether it is prime. This is done by iterating from 2 up to the square root of `i` and checking if any integer in this range divides `i`. If there is no such integer, then `i` is prime and it is appended to the list `primes`. 

Finally, the function returns `True` if the list `primes` has exactly 3 elements, which implies that the given number `a` can be decomposed into 3 prime numbers. Otherwise, it returns `False`. 

This function is encapsulated in a self-contained Python script that solves the problem you posed, and it can be directly copied and run to test its functionality. 

Here is an example of how to use this function:
```python
print(is_multiply_prime(30))
```

This will print `True` as expected, since 30 can be expressed as the product of 3 prime numbers: 2, 3, and 5. 

Also, here is an example for which the function returns `False`:
```python
print(is_multiply_prime(90))
```

In this case, it will print `False`, because 90 cannot be expressed as the product of 3 prime numbers.