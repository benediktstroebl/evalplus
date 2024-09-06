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

In the above code, the is_prime function checks if a number is prime or not. The x_or_y function uses this function to decide whether to return x or y based on the primality of n. The tests ensure that the function works as expected for the provided examples.  Any prime number less than or equal to 1 or 3 will be considered prime. Additionally, the is_prime function uses an optimized approach for checking primality, where it starts checking divisibility from 5 and incrementing by 6 at each step, improving efficiency compared to checking all integers up to n. 

The code efficiently solves the problem and passes the given tests.  It can handle larger prime and non-prime numbers as well.  The code can be optimized further using More Efficient Primality Testing Algorithms like the Sieve of Eratosthenes for even better performance if the prime checking step was a bottleneck in a real-world scenario.  If you want to optimize it further, you may want to use these techniques if you are dealing with large numbers or very performance-sensitive applications, otherwise the given code is already efficient and well-suited for most practical cases.