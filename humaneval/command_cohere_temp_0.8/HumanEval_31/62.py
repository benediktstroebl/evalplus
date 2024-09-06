```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function `is_prime` takes an integer `n` as input and checks if it is prime or not. It employs a optimized algorithm that only checks the divisibility of a number from 2 up to its square root. The function returns `True` if the number is prime and `False` if it is not. 

Here is an example of how to use the function:
```python
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```
This will output accordingly as `True` or `False` depending on whether the number is prime or not.  The given test cases correspond to the problem statement and demonstrate the function's correct behavior.  This code can be copied and pasted into a Python environment or script to solve the problem directly within the specified code block.  If you have trouble executing the code, let me know so I can assist you.