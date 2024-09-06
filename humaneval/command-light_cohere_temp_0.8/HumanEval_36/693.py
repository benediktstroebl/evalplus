Here's the solution:
```python
def fizz_buzz(n: int) -> int:
    cnt = 0
    for i in range(2, n+1):
        num = 0
        while i % 11 == 0 or i % 13 == 0:
            num += 1
        if num > 7:
            cnt += 1
    return cnt
```
This code calculates the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function iterates through numbers from 2 to n, and during each iteration, it checks if the current number is divisible by 11 or 13. If the number is indeed 7, it increments the count variable. The loop continues until the numbers reach the upper limit of n.