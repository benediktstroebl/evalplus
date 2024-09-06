```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    result = []
    while x > 0:
        result.append(str[x(x % base))
        x = x // base
    return ''.join(''.join(result) or '0')

# Test cases
test_1 = [8, 3]
test_2 = (8, 2)
test_3 = (7, 2)

test_results = [change_base(**test) for test in [test_1, test_2, test_3]]

for case, expect in zip(test_results, [''.join expected(''.join(['22', '1000', '111'])))
```