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

This function examines every possible pair in the list 'l' and uses a set 'seen' to keep track of integers that have been seen. The function returns True if it finds two distinct elements in the list that sum to zero and False otherwise. 

Here is a simple test suite that can be used to validate the function:
```python
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
``` 
This will help ensure that the function remains correct over time. Please let me know if this solution suits your needs or if you have any further questions!