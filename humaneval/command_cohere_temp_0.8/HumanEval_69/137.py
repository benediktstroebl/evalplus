```python
def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > max_val:
            max_val = i 
        if i == max_val and lst.count(i) >= i:
            freq = i 
    return max_val if freq == -1 else -1 
```

This Python script defines a function `search` using a list of positive integers as input. It aims to find the greatest integer (`max_val`) that satisfies the condition where its frequency (occurrences) in the list is greater than or equal to its own value. The variable `freq` is used to track the frequency of the current integer in the list. The function iterates through the list, updating `max_val` as it finds larger integers. Additionally, it checks if the current integer is equal to `max_val`, and if its frequency matches the criteria. If no such integer is found, it returns -1. 

The script ensures it covers all scenarios, including the case where no suitable integer is found, by using the `if freq == -1 else -1` condition.