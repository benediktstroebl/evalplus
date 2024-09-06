```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n
    
# Test cases
test_cases = [
    (0,),
    (1, '1'),
    (5, '0 5 10 15 20'),
    (6, '0 6 12 18 20')
]

for test_num, expected in test_cases:
    print(f"Test {test_num}: {expected}")
    assert string_sequence(test_num) == expected
```