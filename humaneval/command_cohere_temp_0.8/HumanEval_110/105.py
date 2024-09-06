```python
def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = True
            break
    if not odd:
        return "YES"
    else:
        temp = lst1
        lst1 = lst2
        lst2 = temp
        return "NO"
```

The function **exchange** checks if there is an odd number in **lst1**. If not, it returns **"YES"** since **lst1** can be made entirely of even numbers. If there is an odd number in **lst1**, the function swaps the two lists, and returns **"NO"**, since the even numbers are in **lst2** and there is an odd number in **lst1**.