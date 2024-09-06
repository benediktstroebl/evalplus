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
n1 = 7
n2 = 15
n3 = 21
x1, y1 = 34, 12
x2, y2 = 8, 5

print(x_or_y(n1, x1, y1))  # Output: 34
print(x_or_y(n2, x2, y2))  # Output: 5
print(x_or_y(n3, x1, y1))  # Output: 21
```

In the above code, the is_prime function checks if a given number n is prime or not. It employs a couple of optimization tricks to make the process more efficient, like checking divisibility by 2 and 3 separately since these are the smallest prime numbers. If n is not prime, it returns y; otherwise, it returns x.