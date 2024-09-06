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

In the above code, the is_prime function is a standalone function that checks whether a given number is prime or not. The x_or_y function relies on is_prime to determine whether n is prime; it returns x if n is prime and y otherwise. 

The test cases are also included to validate the correctness of the x_or_y function. 

This code will run the tests and output the correct results:
```bash
34
5
```