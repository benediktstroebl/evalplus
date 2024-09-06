```python
def fizz_buzz(n: int):
    return fizz_buzz_helper(n)

def fizz_buzz_helper(n: int):
    if n <= 7:
        return 0
    elif n % 11 == 7:
        return 1
    elif n % 13 == 7:
        return 2
    elif n % 17 == 7:
        return 3
    else:
        return 4
``` 
This function returns the number of times the digit 7 appears in the sequence of numbers less than n which are divisible by 11 or 13.