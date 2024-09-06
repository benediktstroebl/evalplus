```python
def median(l: list):
    """Return median of elements in the list l"""
    return (sorted(l)[:len(l)//2] + sorted(l)[len(l)//2])/2
```
This Python function median takes a list l as input and returns the median of its elements. The function first sorts the its input list in ascending order using the sorted() function with a copy of the list l and a slice of length length(l)//2, which means the first half of the elements will be considered. After that, it adds the sorted elements back into the list and divides the result by 2, which effectively gives the median value. 
This function is self-contained and can be used to solve the problem for any given list.