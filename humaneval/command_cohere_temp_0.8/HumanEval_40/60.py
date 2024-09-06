```python
def triples_sum_to_zero(l: list):
    seen = set()
    for i in l:
        for j in l:
            if i != j and j - i in seen:
                return True
            seen.add(i)
    return False
```

This function iterates over each element in the list and checks for combinations of two elements and their differences with other elements in the list. If the difference exists in the set, it returns True, indicating that there are three distinct elements in the list that sum up to zero. Otherwise, it returns False. It utilizes a set data structure to efficiently check for membership of differences.