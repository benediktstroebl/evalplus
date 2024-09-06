```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    if even_found:
        return "YES"
    else:
        return "NO"
```

The function employs the `any()` function with a mapping operation to swiftly ascertain whether `lst1` contains any even numbers, by determining whether any of the elements in `lst1` are even. If even numbers are found in the list, it returns "YES" since the task of exchanging elements from `lst2` to make all elements in `lst1` be even numbers is achievable. If the list contains only odd numbers, it returns "NO" since such an exchange is impossible. This approach ensures efficiency and readability.  This problem can be challenging to solve intuitively, but this solution uses some advanced Python functionalities.