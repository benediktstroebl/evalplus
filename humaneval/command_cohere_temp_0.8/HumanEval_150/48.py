```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Tests
n = int(input("Enter a number: "))
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if x_or_y(n, x, y) == x:
    print("PRIME")
else:
    print("NOT PRIME")
```

This code defines a function `x_or_y` that takes in three arguments: an input number `n`, and two values `x` and `y` (with `x` being returned if `n` is prime, and `y` otherwise). The code uses a `is_prime` function to determine if `n` is a prime number or not. The `is_prime` function loops through numbers from 2 to the square root of `n`, if it finds that `n` is divisible by any of these numbers, it returns `False`. If `n` is not divisible by any of these numbers, it is a prime number and `is_prime` returns `True`. 

The code then asks the user for a number and assigns it to the variable `n`, two supplementary values `x` and `y`, and finally prints out the result of the calculation of the `x_or_y` function. 

If the result is equal to `x`, the program prints "PRIME", and if it's equal to `y`, the program prints "NOT PRIME". 

You can input any 15-digit number and see how the algorithm works with the provided example in the comment. 
If you want to further test the code you can also add additional tests by inputting different numbers and comparing if the output is `x` or `y`. G