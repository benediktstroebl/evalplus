```python
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number and returns the closest integer to it.
    If the number is equidistant from two integers, round it away from zero.

    Examples:
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
   
    15
    Note:
    Rounding away from zero means that if the given number is equidistant from two integers,
    the one you should return is the one that is the farthest from zero. For example,
    closest_integer("14.5") should return 15.0, closest_integer("-14.5") should return - hot

    def test_closest_integer():
    '''
    Test the closest_integer function with different input values
    and verify the output.

    Examples:
    >>> test_closest_integer()
    '''

    return closest_integer("10") == 10 and closest_integer("15.3") == 15

if test_closest_integer():
    print("The function passed the tests!")
else:
    print("The function failed the tests!")
```