```python
def is_sorted(lst):
    lst.sort()   
    seen = set()
    for v in lst:
        if v in seen:
            return False
        seen.add(v)
    return True
```

The function first sorts the list and then uses a set to keep track of the unique elements to check for duplicates, it returns False if any duplicate appears more than once in the list. 

One approach to improve its performance is to use a hashmap (`dict`) instead of a set, since it has a more efficient `O(1)` lookup time compared to a set (`O(n)`). 

Would you like to make any other improvements or optimizations to the given code? Feel free to ask for more tips and insights.