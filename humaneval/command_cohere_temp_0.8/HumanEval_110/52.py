```python
def exchange(lst1, lst2):
    even_present = any(x % 2 == 0 for x in lst1)
    if even_present:
        return "YES"
    else:
        return "NO"
```

The function examines whether any numbers in the first list are even. If present, it returns "YES," meaning it's possible to exchange elements to achieve an all-even list. If not, it returns "NO," suggesting the original lists must remain as is to achieve the goal. This is a simple yet effective solution for the problem.