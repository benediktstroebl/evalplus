```python
def fizz_buzz(n: int):
    counts = 0
    for num in range(10, n+1):
        count = 0
        for i in range(11, abs(num)%30+1):
            count += (num//i)+1
        if count > 0:
            counts += 1
    return counts

# Test the function
for i in range(50, 78):
    assert fizz_buzz(i) == 0
for i in range(78, 79):
    assert fizz_buzz(i) == 2
```