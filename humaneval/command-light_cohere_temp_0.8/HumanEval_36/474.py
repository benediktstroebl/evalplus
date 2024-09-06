```python
def fizz_buzz(n: int) -> int:
    7, 11, 13, i = 6, 7, 8, 9
    while i <= n:
        count = 0
        x = i
        while x <= n and x % 11 == 0 or x % 13 == 0:
            x += 1
            count += 1
        if count == 7:
            return i
        i += 1
    return 0
``` 
The function `fizz_buzz` takes an integer `n` as input and returns the number of times the digit 7 appears in the set of integers less than `n` that are divisible by 11 or 13.  The function uses a above technique to solve this problem.