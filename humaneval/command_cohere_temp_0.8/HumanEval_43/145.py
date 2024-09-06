```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and (i - l.count(i)) % 2 == 0:
            return True
        seen.add(i)
    return False
```

This function takes a list of integers l as input and returns True if there exist two distinct elements in the list whose sum is zero, and False otherwise. To achieve this, it uses a hashset 'seen' to keep track of the elements already encountered. It iterates over the list, and for each element i, it checks if i is larger than zero and not previously seen in the set 'seen'. Additionally, it checks if the parity of the count of i in the list is odd using [(i - l.count(i)) % 2 == 0]. If both conditions are met, it returns True, indicating that there are two distinct elements whose sum equals zero. Otherwise, it marks the element as seen and continues iterating through the list until it finds a pair that sums up to zero or has checked all elements.