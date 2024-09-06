```python
def sort_third(l: list):
    """Sorts a list l such that the elements not divisible by three are in their correct positions, while the values divisible by three are kept as they are in l."""
    return sorted(l, key=lambda x:int(x) if x.is_odd(x) else x)  

def is_odd(x: int):
    """Returns True if x is odd, False otherwise."""
    return x%2 == 1

# Example usage
l = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(l)) 
``` 
This script defines a function sort_third that takes a list l as input and sorts it such that the elements not divisible by three are in their correct positions, while the values divisible by three are kept as they are in l. The is_odd function returns True if the given number is odd, and False otherwise.