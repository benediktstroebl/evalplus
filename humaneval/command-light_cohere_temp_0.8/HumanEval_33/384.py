```python
def sort_third(lst):
    """Sorts a list l such that values that are divisible by three are in their correct order."""
    return sorted(lst, key=lambda x:int(x)//3)
# Example usage:
if __name__ =='__main__':
    lst = [1, 2, 3]
    print("Original list:", lst)
    print("Sorted list:", sort_third(lst))
    lst = [5, 6, 3, 4, 8, 9, 2]
    print("Original list:", lst)
    print("Sorted list:", sort_third(lst))
```
The script defines a function `sort_third` that sorts a list such that the values divisible by 3 are in their correct positions. The function uses the value of the element as a key to sort by and returns the sorted list.