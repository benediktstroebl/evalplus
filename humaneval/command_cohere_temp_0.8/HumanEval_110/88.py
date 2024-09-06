```python
def exchange(lst1, lst2):
    even_present = any(x % 2 == 0 for x in lst1)
    if even_present:
        return "YES"
    else:
        return "NO"
```

The function examines whether any numbers in the first list are even. If present, it returns "YES," indicating that even numbers can be transferred to the second list. If not, it returns "NO," since not all numbers in the first list can be even due to their initial configuration. 

This algorithm solves the problem without requiring additional steps or checking the second list, lst2. Feel free to ask questions if you would like further clarification!