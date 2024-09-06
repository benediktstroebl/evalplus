```python
def fizz_buzz(n):
    count = 0
    for num in range(1, n+1):
        num = str(num)
        if num [0] == 7 and (num [1] <= 4 or num [1] == 7 and num [2] <= 6):
            count += 1
    return count

# Test the function
for i in range(50, 80, 5):
    print(fizz_buzz(i), end='')
```