```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n <= 0:
            continue
        freq[n] = freq.get(n, 0) + 1
        max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```

This Python script defines a function `search` taking a list of positive integers as input. It initializes a dictionary `freq` to store integer frequencies and a maximum value `max_val` set to 0. The function iterates through the list, updating the frequency of each integer in the `freq` dictionary and updating `max_val` if necessary. Then, it checks if `max_val` is less than 1, returning -1 if the condition for the desired integer isn't met. Lastly, it iterates through the `freq` dictionary, returning the value of the integer with its frequency greater than or equal to itself.

Note that this approach uses a dictionary to efficiently track and retrieve the frequencies of integers. This helps determine the answer in a self-contained manner, without using any advanced data structures or additional space beyond what's needed.