```python
def triples_sum_to_zero(l: list):
    seen = set()
    for a in l:
        if a > 0:
            b = -a
        else:
            b = a
        if b in seen and l.count(a) == l.count(b) == 1:
            return True
        seen.add(a)
    return False
```

This function examines each integer in the list. If the integer is positive, it searches for the number that when added to the first integer produces zero. If the integer is negative, it searches for the number that when added to the absolute value of the first integer produces zero. The function returns True if it finds two other members of the list that satisfy this property and False otherwise.