```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and ((i - 1) in seen or (i + 1) in seen):
            return True
        seen.add(i)
    return False
```

This function examines each integer in the list, using a set data structure to efficiently track which integers have been previously encountered. The goal is to find a pair of distinct elements with a sum of zero, specifically looking for integers that are 1 away from another element (either greater by 1 or less by 1). If such a pair is found, the function returns True; otherwise, it returns False.

This algorithm has a time complexity of O(n), where n is the size of the input list, as it requires iterating through the list once to check for pairs that sum to zero.