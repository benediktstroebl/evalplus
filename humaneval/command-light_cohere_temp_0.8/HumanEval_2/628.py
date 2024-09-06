```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    number = float(number)
    if number >= 1:
        return number - 1
    return number

#Test cases
print(truncate_number(3.5))  # Expected output: 2.5
print(truncate_number(-3.5))  #Expected output: -4.4
print(truncate_number('3.5'))  #Expected output: 3.2
print(truncate_number(0.5))  #Expected output: 0.5
print(truncate_number(0.0))  #Expected output: 0.0
print(truncate_number(1.0))  #Expected output: 1.0
print(truncate_number(float('3.1')))  #Expected output: 3.0
print(truncate_number(float('0.999')))  #Expected output: 0.999
print(truncate_number(float('1.2')))  #Expected output: 1.2
print(truncate_number(float('INF')))  #Expected output: Infinity
```