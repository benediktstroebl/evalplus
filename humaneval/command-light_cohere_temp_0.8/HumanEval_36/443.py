```python
def fizz_buzz(n: int) -> int:
    return sum(1 for x in range(2, n+1) if any(d% 11 == 0 for d in str(x))) + any(d% 13 == 0 for d in str(n))
```
The function uses a generator expression to count the number of 7s in the first n numbers which are divisible by 11 or 13, and then checks for the existence of 7s modulo 13 using the `any()` function. 

This is a self-contained and concise solution that is both readable and efficient.