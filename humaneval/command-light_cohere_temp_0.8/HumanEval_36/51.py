```python
def fizz_buzz(n):
    count_seven = 0
    for num in range(1, n+1):
        num = str(num)
        divisible_by_11 = any(char == '7' for char in num)
        divisible_by_13 = any(char == '1' for char in num) 
        if (divisible_by_11 or divisible_by_13):
            count_seven += 1 
    return count_seven
```