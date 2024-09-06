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
x1, y1 = 34, 12
x2, y2 = 8, 5

print(x_or_y(n1, x1, y1))  # Output: 34
print(x_or_y(n2, x2, y2))  # Output: 5
```

In the above code, the is_prime function checks if a given number n is prime or not. It employs a couple of optimization tricks to make its operations more efficient, like checking divisibility by 2 and 3 separately, and then checking through numbers of the form 6k ± 1, popularly known as Fermat's test. The x_or_y function uses this is_prime function to decide whether to return x or y, based on the primality of the input number n. The given tests are implemented and the output is the expected one.