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

This function examines every element in the list. If the element is positive, it checks if it has previously been seen in the set and if there are more than one occurrence of it in the list. If the element is negative, it checks if (-element) is in the set and if there are more than one (-element) in the list. The function returns True if any of these conditions are satisfied, and False otherwise. 

Here's an example usage of the function with a markdown code block showing the test cases:
```python
# Test cases
assert pairs_sum_to_zero([1, 3, 5, 0]) == False
assert pairs_sum_to_zero([1, 3, -2, 1]) == False
assert pairs_sum_to_zero([1, 2, 3, 7]) == False
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
assert pairs_sum_to_zero([1]) == False
```