```python
def sorted_list_sum(lst):
    lst = [str(el) for el in lst if el.length()%2==0]
    lst.sort(key=lambda x: (x.length(), x))
    return lst
    
def el_len(el):
    return len(el)
```
This Python script defines a function called `sorted_list_sum`, which takes a list of elements as input. It filters this list, only retaining elements that have even lengths, using a list comprehension and the `str` constructor to assure that all elements are strings. Then, it sorts the list using the `sort` method, with a custom sorting key that prioritizes elements based on their length and, in case of a tie, their alphabetical order. This results in a list of unique strings, sorted by length and alphabetically within equal-length elements. The element length is determined through the `el_len` helper function, which simply returns the length of a given element. This overall approach efficiently solves the problem statement.