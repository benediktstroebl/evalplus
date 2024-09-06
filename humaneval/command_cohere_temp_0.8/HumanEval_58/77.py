```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists as parameters and uses the `set` function to remove duplicate elements from both lists. The `intersection` method is then used to find the common elements between the two sets, and the result is sorted using the `sorted` function to ensure that the output is consistent and readable. 

To see this function in action, you can call it with the following input:
```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This will output:
```
[1, 5, 653]
[2, 3]
```

This matches the examples provided in the problem statement. 

This approach is efficient and presents a simple solution to the problem, making it a reliable option for code challenges involving lists and their common elements. 
If no strict limitations on methods and time complexity are provided, it's a sensible go-to option. Faster alternatives exist but may be less readable and suitable for coding challenges unless explicitly requested.