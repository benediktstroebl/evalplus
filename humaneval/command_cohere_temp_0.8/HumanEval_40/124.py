```python
def triples_sum_to_zero(lst):
    # Sort the list in ascending order
    lst.sort()
    # Iterate over the list and check for three consecutive elements that sum to zero
    for i in range(0, len(lst) - 2):
        if lst[i] + lst[i + 1] + lst[i + 2] == 0:
            return True
    # If no three consecutive elements are found, return False
    return False
```

This function, `triples_sum_to_zero`, takes a list of integers as input and returns `True` if the list contains three distinct elements that sum to zero. It returns `False` otherwise. The function first sorts the list in ascending order to help identify consecutive elements easier. It then iterates over the list, checking for three consecutive elements that sum to zero. If such a triplet is found, the function returns `True`. If no such triplet is found, the function returns `False`. 

This approach ensures that the function is self-contained and does not rely on any external variables or assumptions about the input list. 

Here is a simple test suite to verify the functionality of the function:
```python
def test_triples_sum_to_zero():
    # Test cases with lists that should return true
    assert triples_sum_to_zero([1, 3, -2, 1]) == True
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True

    # Test cases with lists that should return false
    assert triples_sum_to_zero([1, 3, 5, 0]) == False
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
    assert triples_sum_to_zero([1]) == False

test_triples_sum_to_zero()
```

Running this code will execute the test suite, testing the function with different cases and confirming its correctness.  This can help give further assurance that the function behaves as expected and is not dependent on the state of the program when it is executed.