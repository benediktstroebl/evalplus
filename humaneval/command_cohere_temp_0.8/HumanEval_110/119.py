```python
def exchange(lst1, lst2):
    o = [x for x in lst1 if x%2 == 0]
    e = [x for x in lst2 if x%2 == 0]
    if len(o) == len(lst1):
        return "YES"
    elif len(e) == len(lst2):
        return "NO"
```
The code defines a function exchange that takes two lists, lst1 and lst2, as input. It checks if it's possible to exchange elements between the two lists to make lst1 contain only even numbers. The function does this by creating two separate lists, o and e, containing only even numbers from lst1 and lst2 respectively. It then checks the lengths of these lists. If the length of o is equal to the length of lst1, it means that all elements of lst1 can be made even by exchanging with elements in lst2, so the function returns "YES". Otherwise, if the length of e is equal to the length of lst2, it means that there aren't enough even numbers in lst2 to make lst1 consist only of even numbers, so the function returns "NO".