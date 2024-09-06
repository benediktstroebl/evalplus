```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and pairs_sum_to_zero(l, i, seen) == True:
            return True
        seen.add(i)
    return False

def pairs_sum_to_zero(l, x, seen):
    if x == 0:
        return True
    if x < 0:
        return pairs_sum_to_zero(l, -x, seen)
    if x > 0:
        return pairs_sum_to_zero(l, x, seen) or pairs_sum_to_zero(l, -x, seen)
```

```
Tests:
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
```
The pairs_sum_to_zero function takes a list of integers l as input. It initializes a set seen to keep track of seen elements to avoid duplicates. It then iterates through the list, considering each element x. 

If x is greater than 0, it checks if there's a pair of elements in the list that sums to zero, using the recursive helper function pairs_sum_to_zero. If found, it returns True. Otherwise, it adds x to the set seen and continues checking with the remaining elements.

If x is less than 0, it recursively checks for pairs that sum to x in the list, considering negative values only.

If x is 0, it returns True, as a pair of that element sums to zero.

The recursive helper function, pairs_sum_to_zero, handles the logic of checking pairs that sum to zero in the list, taking the current element x and the set of seen elements seen into account.
```