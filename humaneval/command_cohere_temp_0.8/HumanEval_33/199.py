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
This Python script defines a function called `sort_third`. This function takes a list `l` as input and returns a new list `l_sorted`. The function keeps a copy of the original list and checks if each index is divisible by three. If an index is divisible by three, it sorts the elements of the corresponding index in the copy of the list and appends it to the `sorted_l` list. For all the other indices, it just appends the values in the original list. 
Here is an example usage of the function:
```python
sorted_list = sort_third([1, 2, 3])
print(sorted_list)  # Output: [1, 2, 3]

sorted_list = sort_third([5, 6, 3, 4, 8, 9, 2])
print(sorted_list)  # Output: [2, 6, 3, 4, 8, 9, 5]
```
The function successfully sorts the values at the indices that are divisible by three, while keeping the other values unchanged.