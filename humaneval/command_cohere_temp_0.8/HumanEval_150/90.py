```python
def is_prime(n):
    if n < 2:
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

# Test cases
n1 = 7
x1 = 34
y1 = 12

n2 = 15
x2 = 8
y2 = 5

print(x_or_y(n1, x1, y1))
print(x_or_y(n2, x2, y2))
```

In the above code, the is_prime function checks if a number is prime or not. The x_or_y function returns the value of x if n is prime and y otherwise. The test cases at the end demonstrate the function's correctness for the given examples from the problem statement. Adjust the values of n, x, and y in the test blocks to match the desired values for testing.  This way, the code provides a clear and concise solution to the problem with the necessary tests.  You can modify the values of `n1`, `x1`, `y1`, `n2`, `x2`, and `y2` according to your needs to test different cases for the `x_or_y` function.  This way, the code provides a solution to the problem while ensuring the function's correctness with the given tests.  If you have any questions, just let me know!