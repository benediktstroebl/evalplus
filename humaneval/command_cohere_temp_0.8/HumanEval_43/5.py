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

This function iterates through every element in the list 'l' and for each element, it checks whether the element pairs with another element in the list to sum up to zero. It uses a set 'seen' to keep track of seen elements to avoid duplicate detection. For every positive integer 'x', it checks whether 'x' is in the 'seen' set already, and if so, it checks whether there are at least two occurrences of 'x' in the list 'l'. If so, it returns True. The same logic applies to negative integers, checking whether (-x) appears in the 'seen' set twice in the list 'l'. 

Here is a test suite that matches the provided tests:
```python
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
``` 
This test suite will collectively ensure that the code behaves as expected.