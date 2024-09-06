```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        return_number = prime_fib(n - 1) + prime_fib(n - 2)
        return(True, return_number)

test_prime_fib = [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, False),
    (8, True),
    (9, False),
    (10, True),
    (11, False),
    (12, False),
    (13, True),
    (14, False),
    (15, False),
]

for test in test_prime_fib:
    print(test[0], end=' -> ')
    assert prime_fib(test[1]) == test[0]
```