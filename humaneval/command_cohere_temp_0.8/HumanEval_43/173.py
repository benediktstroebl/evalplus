```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            complement = -i
            if complement in seen:
                return True
            seen.add(i)
        else:
            seen.add(i)
    return False
```

This Python script defines a function pairs_sum_to_zero that takes a list l as input. It then iterates through the list, checking if each integer is positive. If an integer is positive, it calculates its complement to be zero and checks if that complement has already been seen in the set seen. If it has, this indicates the presence of a pair that sums up to zero, and the function returns True. If no such pair is found after iterating through the list, the function returns False.