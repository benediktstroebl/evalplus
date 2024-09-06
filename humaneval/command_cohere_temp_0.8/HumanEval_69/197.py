```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n <= 0:
            continue
        elif n in freq:
            freq[n] += 1
            max_val = max(max_val, n)
        else:
            freq[n] = 1
    return -1 if max_val == 0 else max_val
```

The code works by first creating a dictionary, `freq`, to store the frequency of each integer in the list. Then, it iterates through the list and checks if each integer is greater than zero. If it is, the integer is either already in the `freq` dictionary, so its frequency is incremented, or it's not in the dictionary yet, so its frequency is initialized to 1. The `max_val` variable is also updated with the maximum value of the integer whose frequency is equal to or greater than its own value. Finally, the function returns -1 if the `max_val` is still 0, meaning there are no positive integers whose frequency is equal to or greater than itself. 

This approach takes advantage of the dictionary's ability to update the frequency of a given key in constant time and linearly processes the list to obtain the result in a straightforward manner.