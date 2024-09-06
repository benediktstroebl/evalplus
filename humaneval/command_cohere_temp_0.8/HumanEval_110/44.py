```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    count_odd_in_lst2 = sum(map(lambda x: 1 if x % 2 != 0 else 0, lst2))
    return "YES" if even_found and count_odd_in_lst2 > 0 else "NO"
```

The approach uses lambda functions for readability and a sum function to count the odd numbers in lst2. This solution doesn't require any external libraries. I hope this helps and lets you solve your problem efficiently! Let me know if you have any more questions.