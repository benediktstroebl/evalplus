```python
def exchange(lst1, lst2):
    o = [x for x in lst1 if x % 2 == 0]
    e = [x for x in lst2 if x % 2 == 0]
    if len(o) == len(lst1):
        return "YES"
    elif len(e) == len(lst2):
        return "NO"
```
The code defines a function `exchange` taking two lists `lst1` and `lst2` as parameters. The function body performs two lists` oligy` and `even` collections of even and odd numbers from `lst1` and `lst2`, respectively. The code first checks if the length of the `oly` list is equal to the length of `lst1`, and accordingly returns either "YES" or "NO" versus checking the length of `even` against `lst2`. 
This solution allows us to quickly separate odd and even numbers within the lists, determining their counts and returning the appropriate response. 
The function returns "YES" if it's possible to exchange elements between `lst1` and `lst2` to obtain a list of only even numbers, and "NO" otherwise. The approach is simple to understand and efficient in tackling the problem.