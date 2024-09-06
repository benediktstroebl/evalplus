```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. The `sorted` function is then applied to organize the resultant set's elements in ascending order. The result is a list of unique common elements in both input lists. 

This function adheres to the problem's expected behavior, as illustrated in the example usage included in the original prompt:
```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))

# Example usage
l1 = [1, 4, 3, 34, 653, 2, 5]
l2 = [5, 7, 1, 5, 9, 653, 121]
print(common(l1, l2))  # Output: [1, 5, 653]

l3 = [5, 3, 2, 8]
l4 = [3, 2]
print(common(l3, l4))  # Output: [2, 3]
``` 

The function should efficiently handle any list inputs and deliver the expected unique common elements. Feel free to adapt this solution according to your specific requirements or explore other approaches.