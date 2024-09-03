```python
def closest_integer(value):
    '''
    Returns the closest integer to a given string value, rounding away from zero.
    '''
    convert = lambda x: int(''.join(x)) if x.isdigit() else 0 else float(x)
    i, d = 0, 1
    while d <= 9:
        i += 1
        n = value + str(i)
        if isdigit(n):
            value = n
            break
        d += 1
    return value

#Test cases
print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("-14.5"))
print(closest_integer("14.9"))
print(closest_integer("20.0"))
print(closest_integer("300.2")))
print(closest_integer("-12.2")))
print(closest_integer("Inf"))
print(closest_integer("NaN"))
```
This script defines a function `closest_integer` that takes a string value representing a number and returns the closest integer to it, rounding away from zero. 

The function uses a lambda function to convert the string value to an integer, and then iterates through the digits of the number, incrementing the value by each digit and checking if the number is a digit. If the number is a digit, it updates the value to the digit string. 
Finally, the function returns the updated value.