```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Tests
n = 7
x = 34
y = 12
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}') # Should print "34"

n = 15
x = 8
y = 5
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}') # Should print "5"
```

This script defines a function `x_or_y(n, x, y)` that takes three arguments, `n` (which is presumed to be a number), and two values, `x` and `y`, and returns `x` if `n` is prime and `y` otherwise. To do so, it utilizes the `is_prime` function to determine whether `n` is prime. The script then includes two examples that test the function with specific inputs and print the expected outputs. 

The `is_prime` function itself is also encapsulated within the script. It's a basic optimization function that checks whether a number is prime or not. It returns True if the number is less than or equal to 3, as such numbers are prime by definition. If the number is less than or equal to 1, it returns False, as these numbers are not prime. If the number is even or divides by 3, it returns False, as these numbers are not prime either. Finally, for all other cases, it iterates through a series of numbers, starting from 5, and checks if the number is divisible by them or their successors. If at any point the number is divisible, it returns False; otherwise, it returns True. 

The script overall provides a concise and efficient way to determine whether a number is prime and applies this method to solve the problem.