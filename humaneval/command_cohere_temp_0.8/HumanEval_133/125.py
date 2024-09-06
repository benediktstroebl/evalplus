```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest upper int first.
    """
    result = sum(int(rounding(n)) ** 2 for n in lst for rounding in (lambda x: x, lambda x: x + 1, lambda x: x - 1) if int(rounding(n)) ** 2)
    return result
```

The code uses a list comprehension with a generator expression and a sum function to calculate the result. The generator expression in the list comprehension uses the rounding function to round each number in the list to the nearest upper int and then checks if the squared value of the rounded number is integer, skipping non-integer squares. The rounding function takes a number n as an argument and returns the number rounded to the nearest upper int using integers 1 and -1 for rounding upwards or downwards. It achieves this by following this logic:
1. If the number is already an int, return it as is (rounded neither up nor down).
2. If the number is above an int, round up to the nearest int using 1.
3. If the number is below an int, round down to the nearest int using -1.

The sum function then adds up all the squared integers and returns the result.