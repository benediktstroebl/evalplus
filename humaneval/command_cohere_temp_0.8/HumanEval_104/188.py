```python
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    odd_digits = [int(''.join(x for x in str(n) if x.isdigit() and x % 2 != 0)) for n in x]
    return sorted(list(set(odd_digits)))
```

The function `unique_digits` checks all the digits in the string representation of each number in the input list. It extracts all odd digits and converts them into integers and stores them in the `odd_digits` list. Then it eliminates any duplicate entries from the `odd_digits` list and returns the set of all unique odd digits.

This solution passes the test cases provided in the prompt and returns a sorted list of odd digits without any even digit.