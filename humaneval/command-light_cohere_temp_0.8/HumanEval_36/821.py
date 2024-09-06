```python
def fizz_buzz(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    count = 0
    for num in range(1, n+1):
        if num % 11 == 7 or num % 13 == 7:
            count += 1
    return count

# Test the function
for i in range(80):
    if fizz_buzz(i) == 0:
        print(f"7 does not appear in numbers less than {i} which are divisible by 11 or 13.")
    else:
        print(f"7 appears {fizz_buzz(i)} times in that range.")
```