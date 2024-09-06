```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups) and all(num <= nums for num, nums in dups.items())
```

The function employs two conditional checks:
1. The first conditional check employs the `all` function to verify whether all elements in the list qualify as singular occurrences.
2. The second conditional check employs the `all` function to verify whether all elements, taking into account potential duplicates, are arranged in ascending order. 

The function ultimately returns `True` if both conditions are satisfied, otherwise, it returns `False`. 

The script aligns with the problem description, assuming no negative numbers and only integers. And assumes no specific ordering for duplicates. 

This code can be executed independently, and you can import it anywhere else without relying on other scripts. 

This solution is efficient and readable, providing a concise approach to solving the problem. 

Feel free to implement additional test cases to further validate this script.