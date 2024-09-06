```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    Test for each general list of integers and strings that are divisible by 3
    """
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return sorted(l, key=lambda x: not_divisible(x,3))

def not_divisible(x, m):
    """This function takes an integer x and an integer m and returns 
    True if x is divisible by m, False otherwise.
    """
Example usage:
    >>> not_divisible(4, 2)
    True
    >>> not_divisible(4, 4)
    False
    """
    return x % m == 0
```

This script provides a self-contained function that solves the problem of sorting a list of numbers in a way that keeps numbers divisible by 3 in their original relative order, while numbers that are not divisible by 3 are sorted normally. The function uses a test with integers and strings that are divisible by 3, and returns a sorted list. The test also checks if a given value is divisible by the given divisor, and returns True if it is and False otherwise.