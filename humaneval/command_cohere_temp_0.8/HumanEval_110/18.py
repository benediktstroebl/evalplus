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
        return "NO"
```

The function `exchange()` checks if there is an even number in `lst1` using a loop. When such a number is found, an optimization technique popularly known as "early termination" is used to promptly return "YES" because the rest of the list consists of odd numbers, and any odd number can be exchanged with an even number from `lst2`. 

Otherwise, the loop will finish without breaking, meaning there is no even number in `lst1`. Therefore, it is not possible to exchange elements between lst1 and lst2 to make all the elements in lst1 to be even. Thus the function returns "NO". 

The code assumes that the input lists `lst1` and `lst2` are not empty, as stipulated in the problem statement.