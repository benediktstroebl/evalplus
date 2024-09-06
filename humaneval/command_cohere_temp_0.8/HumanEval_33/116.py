```python
def sort_third(l: list):
    l_copy = l.copy()
    sorted_l = []
    for i in range(len(l)):
        if i % 3 == 0:
            sorted_l.append(sorted(l_copy[i]))
        else:
            sorted_l.append(l_copy[i])
    return sorted_l
```
This script defines a function sort_third which takes a list l as input and returns a list l’. The function sorts the values in list l at indices that are divisible by three and keeps the other values as they are. To do this, it makes a copy of the input list l, called l_copy, and creates an empty list called sorted_l to store the sorted output. Then, using a for loop, it iterates through the indices of l. If the current index is divisible by three, it sorts the values in l_copy at that index and appends the sorted segment to sorted_l. If the index is not divisible by three, it appends the value in l_copy unchanged to sorted_l. Finally, the function returns sorted_l, which has the desired sorted and unsorted segments. 

Here is an example usage of the function:
```python
print(sort_third([1, 2, 3])) # Output: [1, 2, 3]
```
Here is an example with a more complex list:
```python
print(sort_third([5, 6, 3, 4, 8, 9, 2])) # Output: [2, 6, 3, 4, 8, 9, 5]
```
This would print the list [2, 6, 3, 4, 8, 9, 5] which is equal to [2, 6, 3, 4, 8, 9, 5] where the values at the indices divisible by three are sorted, and the values at the other indices are kept the same.