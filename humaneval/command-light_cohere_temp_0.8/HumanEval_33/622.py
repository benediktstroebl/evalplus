```python
def sort_third(lst):
    """Sorts a list so that elements which are not divisible by three are at the beginning, and elements which are divisible by three are at the end. The list is returned is a list of integers"""
    lst = list(lst)
    return sorted(lst, key=lambda x:int(x)//3 if x%3 == 0 else x%3 + 1)

# Example usage:
print(sort_third([1, 2, 3, 4, 5, 6, 7]))
 ```