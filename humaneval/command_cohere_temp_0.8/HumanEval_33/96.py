```python
def sort_third(l: list):
    l_new = []
    for i in range(len(l)):
        if i%3 == 0:
            l_new.append(sorted([l[i-1:i+1]][0]))
        else:
            l_new.append(l[i-1])
    return l_new
```
This script defines a function sort_third which takes a list l as input and returns a list l_new. The function loops through the list, and at indices that are divisible by three, it appends the sorted value of the corresponding index of l to l_new. At other indices, it simply appends l's value to l_new. This method ensures that the list l_new maintains the original values at non-divisible by three positions while sorting the values at divisible by three positions.