```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
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

This code defines a function `x_or_y()` that takes three arguments (`n`, `x`, `y`) and returns `x` if the integer `n` is prime and `y` if n is not prime. It also defines a function `is_prime()` that checks if a number is prime or not. 

To run the tests, the script prompts the user to enter a number (`n`), as well as the corresponding values of `x` and `y`. It then checks whether `x_or_y(n, x, y)` returns `x`, and prints 'PRIME' or 'NOT PRIME' accordingly. 

By invoking this script, you can test different input values and verify the behavior of the `x_or_y()` function based on primality. 
Feel free to customize the tests by modifying the values of `n`, `x`, and `y` to validate different cases.  If needed, I can explain the code in detail and answer any questions you might have.