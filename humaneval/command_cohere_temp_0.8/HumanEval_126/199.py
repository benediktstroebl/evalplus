```python
def is_sorted(lst):
    return all(lst[i] == lst[i+1] for i in range(len(lst)-1)) and len(set(lst)) == len(lst)
```
```
This function checks if the list is sorted in ascending order and if there's only one occurrence of each number in the list. It uses the `all()` function to check if each number is consecutively equal to the next number in the list. It also checks if the length of the set of unique elements in the list is equal to the length of the list, which verifies that there is only one occurrence of each number.
```