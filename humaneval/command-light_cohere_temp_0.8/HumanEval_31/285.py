```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True

# Test the function
for i in range(2, 6):
    print(is_prime(i), end=" ")
print()

for i in range(10, 61, 6):
    print(is_prime(i), end=" ")
print()

for i in range(1, 13441):
    print(is_prime(i), end=" ")
print()

for i in range(1, 62):
    print(is_prime(i), end=" ")
```