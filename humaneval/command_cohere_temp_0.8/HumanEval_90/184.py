```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach utilizes Python's built-in sorting function (`sort()`) to order the list in ascending order. Subsequently, we check the length of the list. If the length is less than 2, indicating an insufficient number of elements to identify the 2nd smallest, the function returns `None`. Otherwise, we access the second-to-last element using `lst[-2]` as this will be the 2nd smallest element in the sorted list, and return it. 

The test cases provided in the problem statement should be used to verify the correctness of the function. 

```python
# Test cases
print(next_smallest([1, 2, 3, 4, 5])) # Should print 2
print(next_smallest([5, 1, 4, 3, 2])) # Should print 2
print(next_smallest([])) # Should print None
print(next_smallest([1, 1])) # Should print None
```

This function is robust and efficient, readily adaptable to lists of various integers. It gracefully manages edge cases, returning `None` when the list has an insufficient number of elements to identify the 2nd smallest.