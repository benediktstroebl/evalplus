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
    evens = [int(''.join(x for x in el if x.isdigit()) for el in x if el.count(4) % 2 == 1)
            for x in map(''.join, zip(*[iter(el) for el in x] * 10))]
    return sorted([el for el in x if el not in evens])
```

The function exploits the fact that an integer has no even digit if and only if it has an odd number of digits, or in other words, it has an odd number of 4s when written in base 10. Thus, it converts each element of the list to a string and counts the number of dugits, and hence 4s, in the base-10 representation. Elements with an odd count of 4s correspond to elements with no even digits. The function then filters these elements out of the list and returns them sorted.  This algorithm has a time complexity of `O(n log n)` where n is the length of the input list.  This is because the function iterates over each element in the list `n` times and within each iteration, it creates a list of digits `log(n)`.