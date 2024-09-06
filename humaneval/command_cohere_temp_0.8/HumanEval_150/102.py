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

# Test cases
n1 = 7
x1 = 34
y1 = 12

n2 = 15
x2 = 8
y2 = 5

print(x_or_y(n1, x1, y1))  # Output: 34
print(x_or_y(n2, x2, y2))  # Output: 5
```

In the above code, the function `x_or_y` uses the `is_prime` function to determine whether `n` is prime. If it is prime, the function returns `x`; otherwise, it returns `y`.

The test cases provided in the original prompt are incorporated and can be expanded to ensure the function behaves as expected across different scenarios.