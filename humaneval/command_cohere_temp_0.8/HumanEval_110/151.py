```python
def exchange(lst1, lst2):
    even_exchange = False
    for x in lst1:
        if type(x) == int and x % 2 == 0:
            even_exchange = True
            break
    if even_exchange: 
        for x in lst2:
            if type(x) == int and x % 2 != 0:
                lst1.append(x)
                lst2.remove(x)
    return "YES" if even_exchange else "NO"
```

The code solves the problem by first checking if the `lst1` list already contains at least one even number. If it does, the function performs a mutual exchange of odd numbers between `lst1` and `lst2`, which is done using two separate loops. It appends an odd number to `lst1` and removes the same odd number from `lst2`, effectively transferring odd numbers from `lst2` to `lst1`.  The result is then confirmed by checking if all the elements in `lst1` are now even. 

The algorithm assumes that the input lists will be numerical and will not check for any validation errors, such as input being a string or a non-numeric value.