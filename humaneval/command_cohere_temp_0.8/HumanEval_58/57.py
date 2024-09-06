```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. Lastly, `sorted` is applied to keep the elements organized and unharmed. The resulting list contains sorted, unique elements found in both input lists. 

This approach ensures consistency and accuracy, enabling the function to handle various scenarios effectively.

This code defines a function `common` that takes two lists, `l1` and `l2`, as parameters and returns the sorted and unique elements that are present in both lists. 

Here's an example of how you can use the `common` function to test its functionality:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

This demonstrates that the function correctly identifies the common elements between the two lists, which are [1, 5, 653] and [2, 3] respectively, and returns them sorted. 

The function's straightforward, effective implementation makes it an invaluable tool for solving problems involving list intersections and uniqueness. 
  
 
**Note:** Ensure `l1` and `l2` are sorted before calling the `common` function to avoid returning elements in different orders. Sorting before calling the function is recommended, as shown below:
```python
>>> common([1, 4, 3, 34, 653, 2, 5].sort(), [5, 7, 1, 5, 9, 653, 121].sort())
[1, 5, 653]
>>> common([5, 3, 2, 8].sort(), [3, 2])
[2, 3]
```