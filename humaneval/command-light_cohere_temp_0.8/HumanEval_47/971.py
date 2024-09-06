```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# test function
def test():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([5, 5]) == 5.0
```

This code defines a function median that computes the median of a list of numbers. The function handles both cases: the list has an odd or even number of elements. The test function contains some test cases that verify the correctness of the median function with different input lists.