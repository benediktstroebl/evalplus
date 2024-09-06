```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    """
    integer = 0
    while number > 1:  #start with 2 as 1 is always 1 and > 1 is needed for the condition
        number -= (number % 10)
    integer += 1
    return (number + integer) if number != 0 else 0

#test cases
print(truncate_number(3.5)) #0.5
print(truncate_number(1.2)) #1

print(truncate_number(0.1)) #1
print(truncate_number(1e9)) #9.0
print(truncate_number(1))  #1
```