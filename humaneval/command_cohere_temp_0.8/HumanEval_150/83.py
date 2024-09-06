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

In the above code, the function `x_or_y` takes in three parameters (`n` (input number), `x` (value to return if `n` is prime), and `y` (value to return if `n` is not prime)). This function utilizes the `is_prime` function to determine if the input number is prime. It returns the value of `x` if `n` is prime and `y` otherwise.

The test cases printed out in the script demonstrate that the function `x_or_y` correctly solves the problem as intended. One example returns the value of `x` (34) because the input number (`n1`) is prime, while the other example returns the value of `y` (5) because the input number (`n2`) is not prime.