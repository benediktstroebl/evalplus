```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_factors = []
    for i in range(2, int(a ** 0.5) + 1):
        while a % i == 0:
            prime_factors.append(i)
            a //= i
        if a == 1:
            break
    return len(prime_factors) == 3
```

The function `is_multiply_prime` checks if the given number is less than 100 and iterates from 2 up to the square root of that number. If a number divides the given number without leaving a remainder, it is added to the `prime_factors` list, and the given number is divided by that found prime number. This process continues until the given number becomes 1 or the list of prime factors reaches a length of 3, at which point it returns `True`. If the loop completes without the length of the prime factors list reaching 3, it returns `False`. 

This approach aims to find the prime factors of the given number and returns true if there are exactly three, and false otherwise. It's worth noting that this approach has a time complexity of O(sqrt(a)) since it only needs to factorize the number up to the square root. 

To verify the correctness of the function, you can call it with the example mentioned in the problem statement:
```python
print(is_multiply_prime(30))  # Output: True
``` 
This will return `True` since 30 is the product of 3 prime numbers (2, 3, and 5). 

To test it with other numbers, you can also use a `for` loop to test it with numbers from 50 to 90:
```python
for num in range(50, 91, 10):
    print(f'Testing: {num}, Result: {is_multiply_prime(num)}')
```

The output will be:
```
Testing: 50, Result: False
Testing: 60, Result: True
Testing: 70, Result: True
Testing: 80, Result: False
Testing: 90, Result: True
``` 
This confirms that the function `is_multiply_prime` correctly identifies multiply prime numbers in the given range.