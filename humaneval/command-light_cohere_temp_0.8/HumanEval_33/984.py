```python
def sort_third(lst):
    """Sorts the list l such that all the values divisible by three are at the beginning"""
    return sorted(lst, key=lambda x: not_divisible(x), reverse=True)
 
def not_divisible(num):
    return num//3 == 0
 
# Test the function
lst = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(lst)) 
```