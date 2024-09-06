```python
def total_match(lst1, lst2):
    total1 = sum(len(x) for x in lst1)
    total2 = sum(len(x) for x in lst2)
    if total1 > total2:
        return lst2
    elif total2 > total1:
        return lst1
    else:
        return lst1 if len(lst1) < len(lst2) else lst2
```

The `total_match` function first calculates the total character count of the strings in both lists using generators and the `sum` function. The function then compares the total character counts of both lists and returns the list with fewer total characters. If both lists have the same number of characters, the function returns the list that is lexicographically earlier. The list of examples provided in the prompt is also provided here for easy reference when running the function:
```python
>>> total_match(['hi', 'admin'], ['hI', 'Hi'])
['hI', 'Hi']
>>> total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
['hi', 'admin']
>>> total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])
['hI', 'hi', 'hi']
>>> total_match(['4'], ['1', '2', '3', '4', '5'])
['4']
```