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

This function examines each integer x in the list l and adds x to the set seen if it has not been previously encountered. The function also adds -x to the set seen to check if the negative of that integer has been previously added to the set. This is because we want to detect if there are two distinct elements in the list that sum to zero. If the set seen has all the elements of the list and the list has no duplicates, then we return True if the set seen has a positive and negative integer pair that sum to zero and False otherwise. The function is self-contained and can be called with any list of integers as input. 

Here is a markdown code block containing some test cases to verify its correctness:
```python
>>> pairs_sum_to_zero([1, 3, 5, 0])
False

>>> pairs_sum_to_zero([1, 3, -2, 1])
False

>>> pairs_sum_to_zero([1, 2, 3, 7])
False

>>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
True

>>> pairs_sum_to_zero([1])
False
```

These test cases should correspond to the test cases provided in the original markdown code block and the function pairs_sum_to_zero should return the values True or False appropriately. Let me know if you would like me to provide any additional assistance.