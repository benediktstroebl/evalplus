```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
``` 

This function returns true if the given number is prime, and false otherwise. It checks if the given number is less than 2, returns false. If it's greater than 2, it iterates from 2 to the square root of the number and checks if the number is divisible by any of these integers. If it is, it returns false. If it isn't, it returns true. The tests provided in the prompt return true for prime numbers and false for non-prime numbers. Here are the test cases and the expected output:
```python
# Testing the is_prime function
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
This is the expected behavior of the function considering the tests. You can add this function to a Python environment to be used in other projects that may require prime number checks. To better understand the underlying concepts of prime numbers and how this function works, you can check out the following:
- [What are prime numbers?](https://www.mathsisfun.com/numbers/prime-numbers.html)
- [Prime number checking in Python](https://www.geeksforgeeks.org/prime-number-checking-python/)
- [Prime Number Formula](https://www.mathsisfun.com/algebra/factors-prime-numbers.html)