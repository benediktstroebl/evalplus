```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif n % 2 == 0 or n <= 5:
        return 5
    else:
        return prime_fib(n-1) + 2

# test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89)
print(prime_fib(6))  # 14
print(prime_fib(7))  # 29
print(prime_fib(8))  # 34
print(prime_fib(9))  # e2)
print(prime_fib(10))  # ja2
```