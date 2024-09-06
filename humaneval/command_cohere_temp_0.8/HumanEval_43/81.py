```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            twice_i = 2 * i
            if twice_i in seen:
                return True
            seen.add(i)
        else:
            seen.add(i)
    return False
```

This Python script defines a function pairs_sum_to_zero that takes a list l as input. It then iterates through the list, if the current integer is positive, it calculates twice_i and checks if it's already present in the seen set. If it is, this indicates a pair that sums up to zero and the function returns True. If not, it adds the current integer to the set. If the current integer is non-positive, it directly adds it to the seen set. Finally, if the end of the loop is reached and no pair has been found, it returns False.