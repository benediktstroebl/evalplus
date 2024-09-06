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
The function **exchange(lst1, lst2)** takes two lists, **lst1** and **lst2**, and returns "YES" if it's possible to exchange elements between the two lists to make **lst1** contain only even numbers. It checks if there's at least one even number in **lst1** and returns "NO" otherwise.  This is because the problem states that the input lists are assumed to be non-empty, so it is not necessary to check if the lists are actually non-empty. 

The code uses a simple **if** statement to check if the list contains an even number, since the actual exchange of elements is not required in the problem statement, the code only needs to determine if such an exchange would be possible.  This solution has a time complexity of **O(1)**.