```python
def is_sorted(lst):
    dups = {}
    for x in lst:
        if x in dups:
            dups[x] += 1
        else:
            dups[x] = 1
    for x in dups:
        if dups[x] > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple dictionary (`dups`) to count the occurrences of each element in the list (`lst`) and checks if any of these occurrences are greater than 1, returning False if so. If not, it then checks if the list is monotonically increasing using the `all` function and a generating expression, iterating through the list pairs and returning True if all comparisons are True, and False otherwise. This solution passes the test cases mentioned in the prompt.