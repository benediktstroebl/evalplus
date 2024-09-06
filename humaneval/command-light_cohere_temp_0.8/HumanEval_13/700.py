```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    # check for repeated divisor
    if a == b:
        return 1
    
    # big O calculation
    temp = 0
    for x in range(1, min(a, b) + 1):
        while a % x == 0 and b % x == 0:
            temp += 1
        a //= x
        b //= x
        
    return temp
```