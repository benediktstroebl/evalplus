Here's the solution:
```python
def truncate_number(n):
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: 
    the decimal part of the number
    """
    return round(n/(n+1)**0.5)
```
And the following test code:
```python
test_truncate = []
test_truncate.append( (1,100) )
test_truncate.append( (2, 2))
test_truncate.append( (2, 100) )
test_truncate.append( (2.8, 1.5) )
test_truncate.append( (0.1, 0.0))
test_truncate.append( (0.5, 1) )
test_truncate.append( (0.01, 0.2) )
test_truncate.append( (0.5, 1.0) )
test_truncate.append( (0.01, 0.0) )
test_truncate.append( (1.01, 100) )
test_truncate.append( (1.00, 1.1) )
test_truncate.append( (1.01, 100) **+ [1.1, 1) )
test_truncate.append( (1.2, 1) )
test_truncate.append( (1.01, 0) + [1.01, 1) )
test_truncate.append( (1.99, 1) )
test_truncate.append( (1.99, 100) )
test_truncate.append( (2, 2.1) )
test_truncate.append( (2, 2) + (1.01, 1))
test_truncate.append( (3, 1) * (0.9 + 1))
test_truncate.append( (4, 0) + (0.5, 1) )
test_truncate.append( (5, 1) + (0.5, 1))
test_truncate.append( (5, 1) + (0.02, 1))
test_truncate.append( (6, 0) + (0.05, 1))
test_truncate.append( (6, 1) + (0.02, 1) + (0.02, 1) )
test_truncate.append( (6, 0) + (0.05, 1) + (0.01, 1) )
test_truncate.append( (7, 1) + (0.01, 1) + (0.01, 1) + (1.01, 1))
test_truncate.append( (8, 1) + (0.01, 1))
test_truncate.append( (8, 100) + (0.1, 1))
test_truncate.append( (8, 100) + (0.5, 1) + (0.01, 1) )
test_truncate.append( (8, 1) + (0.01, 1) + (0.1, 1) )
test_truncate.append( (8, 100) + (0.01, 0) + (0.01, 0) )
test_truncate.append( (8, 0) + (