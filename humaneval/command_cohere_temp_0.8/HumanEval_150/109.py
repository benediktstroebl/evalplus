```python
def is_prime(n):
    """ Checks if a number is prime """
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """ Returns x if n is a prime number, otherwise returns y """
    if is_prime(n):
        return x
    else:
        return y

# Tests
n = int(input("Enter a number: "))
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if x_or_y(n, x, y) == x:
    print("Good Choice!")
else:
    print("Bad Choice!")
```

This script defines a function `x_or_y` that takes in three arguments, a number `n`, and two values `x` and `y`, and returns `x` if `n` is prime and `y` if it is not. 

It also contains a simple test that takes in `n`, `x`, and `y` from the user, calls the function, and prints "Good Choice!" or "Bad Choice!" respectively. 

To run the test, simply run the script with the command line `python x_or_y.py` and it will prompt you to enter `n`, `x`, and `y`. After submitting these values, it will output "Good Choice!" or "Bad Choice!" depending on the values entered. 

Let me know if you have any questions!