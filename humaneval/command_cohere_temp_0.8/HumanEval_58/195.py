```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists as parameters and uses the `set` function to remove duplicate elements from both lists. The `intersection` method is then used to find the common elements between the two lists, and the result is sorted using the `sorted` function. This approach ensures that the resulting list contains only unique, common elements, and provides a consistent sort order. 
The expected behavior for the given examples is:
```python
>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```