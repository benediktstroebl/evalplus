```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n <= 0:
            continue
        freq[n] = freq.get(n, 0) + 1
        max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(max_val, max(lst))
```
The code defines a function `search` taking a list of integers as argument. It initializes a dictionary `freq` to store the frequency of each integer, and initially sets `max_val` to zero. Then, it iterates through the list, updating the frequency of each integer and recalculating `max_val` accordingly. Finally, it returns -1 if `max_val` is less than 1 (meaning no integer has a frequency greater than or equal to itself) or the maximum value in the list if `max_val` meets the condition.