```python
def total_match(lst1, lst2):
    # calculate the total char count in lst1 and lst2
    total1 = sum(len(str(e)) for e in lst1)
    total2 = sum(len(str(e)) for e in lst2)

    if total1 > total2:
        return lst2
    elif total2 > total1:
        return lst1
    else:
        return lst1 if len(lst1) < len(lst2) else lst2
```

The solution utilizes Python's list comprehension and the `sum` function to calculate the total character count in both lists `lst1` and `lst2`. Once the total character counts are determined, the function immediately returns the list with fewer total characters using a logical if-elif-else structure. To handle scenarios where both lists have equal lengths, the function defaults to returning the first list `lst1` since it appears first in the argument order. This strategy ensures simplicity and efficiency in solving the problem.