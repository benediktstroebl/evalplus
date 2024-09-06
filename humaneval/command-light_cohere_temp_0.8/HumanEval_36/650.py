```python
def fizz_buzz(n: int):
    return fizz_buzz_helper(n, 11, 13)

def fizz_buzz_helper(n, num_divisible_by, max_divisor):
    count = 0
    for i in range(1, n+1):
        if i % num_divisible_by == 0 and i <= max_divisor:
            count += 1
    return count

# Unit tests
test_fizz_buzz = []
test_fizz_buzz.py()
assert(fizz_buzz(50) == 0)
test_fizz_buzz.py()
assert(fizz_buzz(78) == 2)
test_fizz_buzz.py()
assert(fizz_buzz(79) == 3)
test_fizz_buzz.py()
```