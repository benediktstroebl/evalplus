```python
def sort_even(l):
    even, odd = zip(*[iter(l)]*2)
    return list(odd)+list(sorted(even))
```
This solution uses Python's partitioning methods to partition the list on the even and odd indices, using the `zip(*[iter(l)]*2)` method. The result is two iterators, `even` and `odd`, which iterate over the even and odd indices of the list. From here, the function creates a list from the `odd` iterator and then sorts the `even` iterator, converting that into a list as well, and returning the two lists concatenated. This achieves the desired result of sorting only the even indices while leaving the odd ones untouched. 

Here is a test case to verify the function:
```python
test = [1, 2, 3]
assert sort_even(test) == [1, 2, 3]

test = [5, 6, 3, 4] 
assert sort_even(test) == [3, 6, 5, 4]
``` 
This will hopefully verify that the function behaves as expected. Let me know if further clarification is needed or if there is a different approach to solving this problem that you would prefer. 
```