```python
def fizz_buzz(n: int):
    if n < 7:
        return 0
    count = 0
    while n % 11 == 0 or n % 13 == 0:
        n /= 13
    count += n // 11
    return count
``` 
This code defines a function fizz_buzz, which aims to solve the problem of counting occurrences of the digit 7 in numbers less than n. The function uses a division to avoid the number 7, and then counts the number of times the resulting number is evenly divisible by 11.