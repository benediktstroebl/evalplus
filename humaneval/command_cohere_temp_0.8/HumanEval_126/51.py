```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in set(dups))
```

This function uses a dictionary to count the occurrences of each unique element in the input list lst. Then, it checks if all non-unique elements have an occurrence count of 1. If so, the list is sorted, and if any element has a count greater than 1, it is not considered sorted. This algorithm has a time complexity of O(n) where n is the number of elements in the input list. 

The previous response adhered to the specified code block format, whereas this one provides a markdown code block with the Python script aligned with the problem description above. Let me know if this aligns better with your request or if I can make any other adjustments to help you with your problem.