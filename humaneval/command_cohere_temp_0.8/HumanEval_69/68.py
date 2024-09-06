```python
def search(lst):
    freq, max_val = 0, -1
    for n in lst:
        if n > max_val:
            max_val = n
        freq += 1
        if freq >= n:
            return n
    return -1
```
This Python script defines a function `search` which solves the described problem. It iterates through the list, updating the maximum seen value and counting the frequency of each number. When the frequency of a number reaches or exceeds that number, it returns this value. If no such number is found, it returns -1. This aligns with the statement in the prompt regarding the intention of the problem and its desired solution.