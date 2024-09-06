Here's a Python script with a self-contained function `fizz_buzz` that solves the problem:
```python
def fizz_buzz(n):
    cnt = 0
    for i in range(1, n+1):
        if i%11==0 or i%13==0:
            cnt += str(i).count('7')
    return cnt
```
The function uses a loop to iterate through integers from 1 to `n` and counts the number of times the digit '7' appears in integers less than `n` that are divisible by 11 or 13. The result is returned as the answer.