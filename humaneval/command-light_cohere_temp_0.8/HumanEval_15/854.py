```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

#Test cases
test_cases = [
    (0,), 
    (1, '1'), 
    (5, '5 4 3 2 1'), 
    (6, '6 5 4 3 2 1'), 
    (10, '10 9 8 7 6 5 4 3 2 1'), 
]

for act, expected in test_cases:
    got = string_sequence(act)
    assert got == expected, f"Test case {act} failed: {got} != {expected}"
```