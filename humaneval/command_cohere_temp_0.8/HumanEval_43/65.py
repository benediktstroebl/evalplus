```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if (-x) in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function examines every element in the list. If the element is positive, it attempts to find another occurrence of that element in the list, either with the same sign or the negative sign, to make their sum equal to zero. If the element is negative, it attempts to find the element with the same absolute value but the opposite sign to sum to zero. The function returns True if any such pair is found, and False otherwise.

Here is a test suite that you can use to test the function:
```python
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
    assert pairs_sum_to_zero([0, 0, 0, 0, 0]) == False
    assert pairs_sum_to_zero([-1, 0, 1, -1, 1]) == True
```

To test the function, you can call the test_pairs_sum_to_zero function, which will check the output of the pairs_sum_to_zero function with the provided test cases and assert that the expected output matches the actual output.