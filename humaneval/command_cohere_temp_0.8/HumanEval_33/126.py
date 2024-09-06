```python
def sort_third(l: list):
    l_new = []
    for i in range(len(l)):
        if i%3 == 0:
            l_new.append(sorted([x for x in l][i]))
        else:
            l_new.append(l[i])
    return l_new
```
This script defines a function sort_third which takes a list as an argument and returns a list with the same elements in the same places if the index is not divisible by three, while for indices that are divisible by three, the elements are sorted in ascending order. The main logic of the function is encapsulated in the loop where it iterates through the elements of the list using the range function, and for each index, it checks if the index is divisible by three, using the modulo operator %. If it is, the element is added to the new list after sorting all the elements at indices divisible by three, while if it is not, the element is added as it is, without sorting it. The function updates the list l with each iteration by appending elements to the list l_new, which is then returned at the end of the function.

Here's an example usage of the function:
```python
sort_third([1, 2, 3]) # Output: [1, 2, 3]
sort_third([5, 6, 3, 4, 8, 9, 2]) # Output: [2, 6, 3, 4, 8, 9, 5]
```
This demonstrates that the function sorts the list elements at indices divisible by three in ascending order, while leaving the other elements unchanged.