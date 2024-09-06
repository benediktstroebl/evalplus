```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as parameters. It uses the `intersection` method to find the unique elements common in both lists, then uses the `set` function to remove duplicates, and finally applies the `sorted` function to sort these common elements. The resulting list contains the sorted unique elements that appear in both input lists. 

To see it in action, you can call the function with the following examples:
```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This should output:
```
[1, 5, 653]
[2, 3]
```

These results are consistent with the provided example outputs in the problem statement. 

This approach has a time complexity of `O(min(len(l1), len(l2)))`, owing to the intersection operation and the sorting step, both of which take linear time with respect to the length of the shorter list. It also has a space complexity of `O(min(len(l1), len(l2)))`, due to the creation of sets for distinct elements. 

Please note that you'll need to install the `sorted` and `set` libraries before running this code. You can do so by running `pip install sorted set` if they are not already installed in your environment.