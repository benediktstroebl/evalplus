```python
def exchange(lst1, lst2):
    even_exchange = False
    for x in lst1:
        if type(x) == int and x % 2 == 0:
            even_exchange = True
            break
    if even_exchange: 
        return "YES"
    else:
        temp = lst1
        lst1 = lst2
        lst2 = temp
        even_exchange = False
        for x in lst1:
            if type(x) == int and x % 2 == 0:
                even_exchange = True
                break
        if even_exchange: 
            return "YES"
        else:
            return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, and checks if the even numbers between the two lists can be moved to `lst1` to make it contain only even numbers. It first checks if there's at least one even number in `lst1`, and if there is, it returns "YES." If not, it swaps the two lists and rechecks, as the function description allows for any number of element exchanges between the two lists, and this is a simpler approach to check for the possibility of even number exchange. The function returns "YES" if at least one list has only even numbers after possible exchanges, and "NO" otherwise.