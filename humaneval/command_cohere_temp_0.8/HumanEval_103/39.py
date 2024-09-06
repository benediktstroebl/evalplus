Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    diff = m - n 
    avg = (n + m) // 2 
    if diff < 0:
        return -1
    binary_representation = bin(round(avg))[2:]
    return binary_representation if binary_representation.isalpha() else '0b' + binary_representation
```
This function:
- Calculates the average of `n` and `m` and stores it in the `avg` variable.
- Calculates the binary representation and ensures it is well-formed with leading '0b' if necessary.
- Checks if the difference between `n` and `m` is negative and returns -1 if so.
- Returns the binary representation of the rounded average. 

The expected output for the given examples in the prompt is:
```
'0b11'
-1
'0b1111'
'0b11010'
```

This script passes the following tests:
```python
test_cases = [
    (1, 5, '0b11'),
    (7, 5, -1),
    (10, 20, '0b1111'),
    (20, 33, '0b11010'),
]

for n, m, result in test_cases:
    assert rounded_avg(n, m) == result
```

You can copy and paste this code into a Python environment or script to test it out.