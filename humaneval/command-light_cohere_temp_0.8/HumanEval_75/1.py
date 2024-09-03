```python
def is_multiply_prime(n):
    s = set()
    while n > 1:
        if n % 2 == 0:
            s.append(2)
        n //= n // 2
        else:
            i = 3
            while i * i <= n:
                if n % i == 0:
                    s.append(i)
                n //= n // i
                i += 2
    return len(s) == 3

# Test cases
test_cases = [10, 22, 30, 58, 66, 70, 57, 113]
for test in test_cases:
    print(is_multiply_prime(test))
```