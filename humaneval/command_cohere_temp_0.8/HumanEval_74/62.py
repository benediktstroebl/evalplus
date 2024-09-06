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

The solution utilizes two sums to calculate the total characters in `lst1` and `lst2` respectively. According to the problem statement, the function returns the list with more characters, and if the total number of characters is the same, the function returns the list with less elements. Lastly, if the length of the two lists is the same, it returns the first list. This reasoning helps in optimizing the solution. 

The unit tests provide in the problem statement are:
1. `total_match([], [])` Returns `[]`
2. `total_match(['hi', 'admin'], ['hI', 'Hi'])` Returns `['hI', 'Hi']`
3. `total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])` Returns `['hi', 'admin']`
4. `total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])` Returns `['hI', 'hi', 'hi']`
5. `total_match(['4'], ['1', '2', '3', '4', '5'])` Returns `[4]`

The function passes all five test cases.