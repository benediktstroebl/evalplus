```python
def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = True
            break
    if odd:
        return "NO"
    else:
        temp = lst1
        lst1 = lst2
        lst2 = temp
        return "YES"
```

The function **exchange** takes two lists, **lst1** and **lst2** as input. It first checks to see if either list contains an odd number. If there's at least one odd number in **lst1**, the function returns "NO," indicating that the exchange can't be done. If **lst1** contains only even numbers, the function swaps the contents of both lists and returns "YES," indicating that the exchange has been successfully performed.