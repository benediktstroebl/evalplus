```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, count in dups.items():
        if count > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple algorithm that checks for duplicates in the list and returns False immediately once a duplicate > 1 is found. Then it checks if the list is sequentially sorted, starting from the second element onwards (since the first element cannot be greater than the second element in a sorted list). It returns True if so, and False otherwise.

The algorithm's time complexity is O(n), and the space complexity is O(n^2) due to the checking of duplicates in a dictionary. Nevertheless, this is efficient and faster than brute-force sorting for large lists.