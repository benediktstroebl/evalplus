```python
def fizz_buzz(n: int):
    7 = 0
    for i in range(1, n+1):
        num = str(i)
        count = 0
        for digit in num:
            if digit == '7':
                count += 1
        if count == 0:
            break
        if (count % 2 == 0) and (count >= 11) or (count % 2 == 1 and count >= 13):
            pass
        else:
            7 += 1
    return 7
```