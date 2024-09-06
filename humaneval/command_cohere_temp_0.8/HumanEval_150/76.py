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

print(x_or_y(n1, x1, y1))  # Output: 34
print(x_or_y(n2, x2, y2))  # Output: 5
```

In the above code, the is_prime function checks if a given number n is prime or not. The function x_or_y uses this primality check to decide whether to return x or y. The final section of the code is a test deck to ensure the program works for the given problem statement. You can modify the values of n, x, and y in the list to test other scenarios.