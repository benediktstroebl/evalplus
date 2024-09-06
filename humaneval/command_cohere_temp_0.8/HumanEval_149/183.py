```python
def sorted_list_sum(lst):
    lst_new = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_new.append(x)
    lst_new.sort()
    for i in range(len(lst_new)):
        if i > 0 and lst_new[i] == lst_new[i - 1]:
            del lst_new[i]
    return lst_new
```
The method utilizes a 'list comprehension' and the 'sort' function to solve the problem depending on the specified rules. Then, to avoid duplicates, it uses a 'sorted' list to eliminate any duplicate elements. This allows the function to meet the specifications of the problem.  This solution has a time complexity of `O(n log n)` due to the combination of the `sort` and `sorted` operations.