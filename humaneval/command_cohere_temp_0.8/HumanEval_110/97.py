```python
def exchange(lst1, lst2):
    even_present = any(lst1)
    if even_present:
        return "YES"
    else:
        return "NO"
```

The function **exchange** takes two lists, **lst1** and **lst2**, as input and returns a string indicating whether it is possible to exchange elements between the two lists to make lst1 a list of only even numbers. The function first checks if there's at least one even number in **lst1** using the **any()** function to short-circuit evaluate whether an element satisfying the condition exists. If there is at least one even number in lst1, it returns "YES", indicating that an exchange can be performed to achieve the desired even-only list. Otherwise, it returns "NO," indicating that no exchange can result in an all-even lst1.