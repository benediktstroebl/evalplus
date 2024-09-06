Here's a Python script that contains a function named `double_the_difference` which follows the specification you provided:
```python
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    '''
    result = 0
    for n in lst:
        if isinstance(n, int) and n > 0:
            if n % 2 == 1:
                result += n * n
        elif n == 0:
            result += 0  # Handle zero correctly
    return result

# Test cases
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0 
assert double_the_difference([1, -1, 1, 1, -1]) == 2
assert double_the_difference([]) == 0
```

This code snippet includes the function `double_the_difference` and a few tests to validate its correctness against the specified behavior. 

If you'd like to further isolate the function for independence, you can encapsulate it within a main guard and conduct the tests separately for full isolation:
```python
def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0 
    assert double_the_difference([1, -1, 1, 1, -1]) == 2
    assert double_the_difference([]) == 0

def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    '''
    result = 0
    for n in lst:
        if isinstance(n, int) and n > 0:
            if n % 2 == 1:
                result += n * n
        elif n == 0:
            result += 0  # Handle zero correctly
    return result
```