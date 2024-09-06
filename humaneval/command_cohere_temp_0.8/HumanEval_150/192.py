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

In the above code, the is_prime function is a helper function that checks if a given number is prime or not. Once this is established, the x_or_y function returns the value of x if n is prime, and y otherwise. 

The test cases are also included to validate the function. 

The logic behind this solution is straightforward. We want to return $x$ if the input $n$ is prime, and $y$ if n is composite (not prime). One way to distinguish between prime and composite numbers is to check if any integers between 2 and $\sqrt{n}$ divide n. If none do, then n is prime, otherwise, it is composite. 

We use the is_prime function for this test. If n is prime, we return x; otherwise, we return y.  This approach is efficient and has a time complexity of $O( \sqrt{n} )$.