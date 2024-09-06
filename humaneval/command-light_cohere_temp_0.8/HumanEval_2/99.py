```python
def truncate_number(n: float) -> float:
    return n if n.isdigit() else float('1' + int(n))  #if number is not a digit, return as isdigit or 1 plus integer of digits.

# test cases
print(truncate_number(3.5)) #0.5
print(truncate_number('3.5')) #3.5
print(truncate_number('a3')) #a
print(truncate_number('abc123')) #123
print(truncate_number(123.456)) #123.456
print(truncate_number(float('3'))) #3
```
The function takes a number and returns the decimal part of it, as if the number is not a digit, then it returns the number as an integer. If the number is a digit, then the function returns the number without changing it.