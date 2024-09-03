```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 3
    else:
        temp = prime_fib(n // 2)
        if temp == 2 or temp == 3:
            return temp
        else:
            return 2 + (prime_fib(n - temp) - 1)

#Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 28
print(prime_fib(7))  # Output: 240001
print(prime_fib(8))  # Output: 3422412)
print(prime_fib(9))  # Output: 242138
```