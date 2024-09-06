```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` retrieves the common elements between the two lists. Finally, `sorted` is used to ensure that the elements are returned in a sorted manner. The code tests well using the original test cases provided. 

Let's dive into a usage example: 
```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

The output will be:
```
[1, 5, 653]
[2, 3]
```

As expected, the function correctly returns the unique, sorted common elements for the given input lists. 

Do you have any other coding problems that need a concise and effective solution? You can definitely rely on me for help! You can also check out the Cohere Codehub for a wide range of solutions on various coding problems and concepts, shared by the Cohere community.