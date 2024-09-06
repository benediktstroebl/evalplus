```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, cnt in dups.items():
        if cnt > 1:
            return False
    return True
```

The function employs a simple algorithm that iterates through the list of items, and for each item, it checks whether the item is already present in the dictionary of duplicates, if so, it increments the occurrence of the same, otherwise, it creates a new entry with the item as the key and 1 as the value. After the loop, it checks whether any item has a count greater than 1, if so, it returns False, if not, it returns True. 

The markdown code block has been provided for you to copy and paste into a Markdown document if needed. You can add this code to see whether it passes the provided tests. 

Please note that this is just one possible solution, there are many other ways you can solve this problem and it may be fun to experiment with different approaches to see which one you prefer.