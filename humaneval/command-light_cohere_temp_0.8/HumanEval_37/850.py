```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return sorted(lst) == even_lst

test_even = [
    [5, 6, 3, 4],
    [1, 2, 3],
    [10, 20, 30],
    [40, 60, 70]
]

print(sort_even(test_even))
``` 
The function 'sort_even' receives a list and returns a list of the even items, then sorts the original list with those elements.  The result then to the solution, it uses a generator expression to create a list of even numbers and then uses the built list to filter the list of elements and returns the sorted list.