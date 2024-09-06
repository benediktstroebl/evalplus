```python
def total_match(lst1, lst2):
    l1_total = sum(len(x) for x in lst1)
    l2_total = sum(len(x) for x in lst2)
    
    if l1_total < l2_total:
        return lst1
    elif l2_total < l1_total:
        return lst2
    else:
        return [x for x in lst1 if x not in lst2]
```

The problem revolves around finding the intersection size of two lists, which is the number of elements that are common to both lists. The `total_match` function works by first calculating the total character length of each list, using `sum()` to iterate through the strings in each list and finding their length with `len()`. 

If one list has a smaller total character length than the other, it is assumed to have no common elements and is returned. If the character lengths are equal, the function iterates through one of the lists and checks if each element is not in the other list, using the list comprehension `[x for x in lst1 if x not in lst2]`. Elements that are not present in both lists are returned. 

The logic is encapsulated within the function, making it self-contained and easy to use, while also providing a clear understanding of how the output is determined.