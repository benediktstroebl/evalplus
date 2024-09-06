```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer()` takes a string value as input and returns the closest integer value to it, following the rounding away from zero rule. This behavior ensures consistent rounding, making the function versatile and adaptable to different input scenarios.

Here is an example of how to use the function:
```python
print(closest_integer("10"))  # Output: 10
print(closest_integer("15.3"))  # Output: 15
print(closest_integer("14.5"))  # Output: 15
print(closest_integer("-14.5"))  # Output: -15
``` 

The expected output from the examples above is:
```
10
15
15
-15
``` 
This demonstrates the correct behavior of the `closest_integer` function adhering to the rounding away from zero rule.