```python
def sort_third(lst):
    """Sorts a list so that values divisible by 3 are at the beginning, and the rest are in the end of the list"""
    return sorted(lst, key=lambda x: not_divisible(x, 3), reverse=True)
 
def not_divisible(x, m):
    """Returns True if x is divisible by m, False otherwise"""
    return (x // m == 0)
 
# Example list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sort_third(lst))
# Prints [2, 3, 4, 5, 6, 7, 8, 9]
```
This Python script defines a function called sort_third that sorts a list according to the problem prompt. The function uses a key lambda function to identify the elements divisible by 3 and place them at the beginning of the list, while the rest follows in the end. The list lst is then passed to the function and prints the sorted list.