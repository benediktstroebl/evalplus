```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if (-x) in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function iterates through every element in the list and simply checks if the absolute value of the number is already in the set, with the condition that the list contains at least two elements that give the same absolute value. This is achieved using a set to avoid duplicate values and prevent any chance of a double count. The function returns True if there are two distinct elements in the list that sum to zero and False otherwise. It is important to note that the function assumes that the input list only contains integers for the logic of the checks to be applicable.