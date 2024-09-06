```python
def total_match(lst1, lst2):
    total1 = sum(len(str(el)) for el in lst1)
    total2 = sum(len(str(el)) for el in lst2)
    if total1 > total2:
        return lst1
    elif total2 > total1:
        return lst2
    else:
        return lst1 if len(lst1) < len(lst2) else lst2
```

The code exploits the sum of characters of all strings within a list to determine which list should be returned based on the condition of the total number of characters. The code then checks if the total character count of one list is greater than the other and returns the list with the least total character count. If both lists have an equal amount of characters, the code returns the list that has fewer strings. This ensures that the list with the most distinct strings that have the highest chance of containing a unique character is returned.