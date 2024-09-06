```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    for num, count in dups.items():
        if count > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```

The function employs a simple algorithm that takes advantage of the list being sorted and potential duplicates. It first checks for elements that appear more than once in the list, recording their counts in the `dups` dictionary. If any count exceeds 1, it returns False as not being sorted. Otherwise, it checks through pairwise comparisons if the list is sorted. The function is succinct and intuitive, suitable for problem-solving tasks. It also avoids the use of complex data structures like sorting algorithms, making it efficient for longer lists.