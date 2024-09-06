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

# Test Cases
n1 = 7
x1 = 34
y1 = 12

n2 = 15
x2 = 8
y2 = 5

print(x_or_y(n1, x1, y1))
print(x_or_y(n2, x2, y2))
```

In the above code, the function `x_or_y` takes in three parameters (`n` (input number), `x` (value to return if `n` is prime), and `y` (value to return if `n` is not prime)). This function utilizes the `is_prime` function to determine if the input number `n` is prime. It then returns the corresponding values of `x` and `y` based on this evaluation.

The test cases, namely `n1`, `x1`, `y1`, `n2`, `x2`, and `y2`, are included to validate the functionality of the `x_or_y` function. These test cases demonstrate the desired behavior of the function, returning the value of `x` when `n` is prime and the value of `y` otherwise. By running the script, we can observe the expected output values for these test cases, confirming that the function behaves as intended. 

This Python script provides an efficient and streamlined way to solve the problem, with the `is_prime` function serving as a useful utility for future prime number checks.