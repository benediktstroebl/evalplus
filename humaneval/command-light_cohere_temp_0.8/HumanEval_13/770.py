```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    max_c = 0
    for i in range(1, min(len(str(a)), len(str(b)) + 1)):
        if str(a)[:i].isdigit() and str(b)[:i].isdigit():
            max_c = max(max_c, int(str(a)[:i] / str(b)[:i]))
        elif i == len(str(a)):
            break

    return max_c
```