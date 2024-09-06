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

This function takes a list of integers l as input and returns True if there exist two distinct elements in the list whose sum is zero, and False otherwise. To achieve this, it uses a hashset (seen) to keep track of the elements already encountered. It iterates over the list, and for each element i, it checks if i is greater than 0, not in the set seen, and if the parity of i minus the count of occurrences of i in l is equal to 0 (i.e., (i - l.count(i)) % 2 == 0). If all these conditions hold, it returns True, indicating that there are two distinct elements in the list with sum zero. If no such pair is found, it returns False.