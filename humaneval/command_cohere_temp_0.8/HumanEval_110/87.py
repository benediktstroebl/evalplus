```python
def exchange(lst1, lst2):
    res = 'NO'
    even_idxs = [i for i, x in enumerate(lst1) if x % 2 == 0]
    if len(even_idxs) > 0:
        for idx in even_idxs:
            lst1[idx], lst2[idx] = lst2[idx], lst1[idx]
        res = 'YES'
    return res
```

The function `exchange()` operates on two lists, `lst1` and `lst2`. It aims to determine whether elements can be exchanged between these two lists to transform `lst1` into a list of only even numbers. The function starts by checking if there are any even numbers in `lst1`, and if there are any, it proceeds to swap elements from `lst1` with those from `lst2` at the corresponding indices. The outcome is then set to 'YES' if any swaps were made, indicating that the transformation is possible, and 'NO' otherwise. 

This problem can be solved in various ways, but this solution focuses on simplicity and efficiency. Feel free to ask questions if you'd like to know more about the solution or discuss other approaches.  If you would like to better understand any concepts involved, remember to ask ahead. Let me know if you would like me to walk through any specific parts of the code in greater detail.