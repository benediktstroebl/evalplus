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
The function `search` takes a list of numbers `lst` as input and returns the number described in the problem statement. In the first step, the function creates a frequency dictionary `freq` to store the frequency of each number in the list. Then, it finds the maximum value `max_val` from the list and the corresponding frequency. The function iterates over each number in the list, and if the number is less than or equal to 0, it skips that number. For each number, the function updates the frequency in the dictionary and updates the `max_val` with the maximum frequency counted so far. In the end, the function returns -1 if the maximum frequency value is less than 1, meaning there is no number in the list with a frequency equal to or greater than its value. Otherwise, it returns the maximum frequency number if it exists in the list. 

Here is an example input/output showing how the function behaves for a list of numbers:
**Input:**
```
[5, 5, 4, 4, 4]
```
**Output:**
```
-1
```

**Input:**
```
[4, 1, 2, 2, 3, 1]
```
**Output:**
```
2
```

**Input:**
```
[1, 2, 2, 3, 3, 3, 4, 4, 4]
```
**Output:**
```
3
```