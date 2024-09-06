```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if -x in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function iterates through the list, tracking positive and negative occurrences of numbers in the 'seen' set. If it encounters a positive number 'x', it checks if 'x' has been seen before and if there are multiple occurrences of 'x' in the list. If so, it returns 'True'. The function performs a similar check for negative numbers, using the set to track occurrences of numbers with a negative sign. If any such pair is found, it returns 'True'. If no qualifying pairs are found, it returns 'False'. 

This approach allows the function to efficiently solve the problem in a single pass through the input list, without requiring additional lists or complex data structures.

Here is a test suite that you can use to test this function:
```python
def test_pairs_sum_to_zero():
    # Test cases with lists provided in the original problem statement
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False

    # Additional test cases
    assert pairs_sum_to_zero([1, 2, -1, 2, -5, 0, -7, 7, -1]) == True
    assert pairs_sum_to_zero([2, -2, 4, 6, 8, -10, -12]) == True
    assert pairs_sum_to_zero([20, 1, -21, 22, 43, 32, -5, 55]) == True
    assert pairs_sum_to_zero([55, -1, -3, 2, 4, 5, -7, 7, -8]) == True

    # Test case with only positive numbers
    assert pairs_sum_to_zero([1, 2, 3, 4, 5]) == False

    # Test case with only negative numbers
    assert pairs_sum_to_zero([-1, -2, -3, -4, -5]) == False

    # Test case with a single element
    assert pairs_sum_to_zero([0]) == False

    # Test case with no elements
    assert pairs_sum_to_zero([]) == False
```

This test suite includes multiple test cases, including edge cases, to validate the behavior of the `pairs_sum_to_zero` function.