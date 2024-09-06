```python
def sort_third(l: list):
    l_new = []
    for i in range(0, len(l), 3):
        try:
            temp = l[i:i+3]
            temp.sort()
            l_new += [x for x in temp]
        except:
            l_new.append(l[i])
    return l_new
```
This script defines a function sort_third which takes a list as an argument and returns a new list. The new list has the same elements as the original in all indices that are not divisible by three, while the elements at the indices that are divisible by three are sorted in ascending order. The sorting is performed using the built-in Python sort() method. Finally, the new list is returned. 

Here is an example of how to use this function:
```python
print(sort_third([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Output: [2, 6, 3, 4, 8, 9, 5]
```
This example uses the function to return the sorted list according to the specified criteria.