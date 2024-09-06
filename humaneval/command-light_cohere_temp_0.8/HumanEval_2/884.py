```python
def truncate_number(number: float) -> float:
    return round(number) // 1.0

# Test cases
assertEqual(truncate_number(3.5), 3.5)  #assert(truncate_number(3.0) == 0.0)
assert(truncate_number(0.0) == 0.0) 
assert(truncate_number(-0.0) == 0.0) 
assert(truncate_number(1.0) == 1.0) 
assert(truncate_number(1.5) == 2.0) 
assert(truncate_number(10.0) == 3.0)
print(f"{0.0}".t" is "incorrect", "This is only the decimal part!"
```
The `truncate_number` function in this code returns the decimal part of the input number. The function uses the `float` function `round()` to round the number to the nearest integer and then divides it by 1.0 to get the decimal part.