```python
def simplify(x, n):
    numerator, denominator = map(float, x. PCM)
    if numerator *denominator:
        x = numerator / denominator
        return x
    return False

# Test cases
test_cases = [
    ("1/5", "5/1"),
    ("7/10", "10/2"),
    ("1/6", "2/1"),
    ("16/8", "2/4"),
    ("12/60", "12/60"),
    ("81/100", "9/25"),
    ("49/25", "13/5")
]

for case in test_cases:
    result = simplify(case[0], case[1])
    print(f"Case {case[0]} : Expected {result}, got {case[1]}")
```