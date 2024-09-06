```python
def fizz_buzz(n: int) -> int:
    if n <= 0:
        return 0
    
    char_count = 0
    is_divisible_11 = False
    is_divisible_13 = False
    
    for digit in str(n):
        if digit == '7':
            char_count += 1
        elif is_divisible_11 and digit == '1':
            is_divisible_11 = True
        elif is_divisible_13 and digit == '4':
            is_divisible_13 = True
    
    if char_count == 0:
        return 0
    elif char_count == 1 and is_divisible_11:
        return 1
    elif char_count == 1 and is_divisible_13:
        return 2
    elif char_count == 2 and is_divisible_11 and is_divisible_13:
        return 3
    
    return char_count
```