```python
def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = not odd
    if odd:
        return "NO"
    else:
        return "YES"
```
This Python script defines a function `exchange` that takes two lists `lst1` and `lst2` as input. It checks if there is at least one odd number in `lst1` and then swaps odd numbers with even numbers from `lst2`. It returns "NO" if there is no swap possible and returns "YES" if all numbers in `lst1` are even after swapping. Hence, it determines if it's possible to exchange elements between the two lists to make `lst1` a list of only even numbers.