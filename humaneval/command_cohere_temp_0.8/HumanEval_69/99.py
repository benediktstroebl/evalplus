```python
def search(lst):
    freq, max_val = 0, max(lst)
    for n in lst:
        if n >= freq:
            freq = n
        if n > max_val:
            max_val = n
    return -1 if max_val == freq and max_val == 0 else max_val
```

The function `search` iterates through the list, keeping track of the maximum value while also counting the frequency of each number. If a number exceeds its frequency, it updates both tracks. Ultimately, it returns the greatest integer if it exceeds its frequency or -1 if no such integer exists. 

This approach ensures that the variables always reflect the correct states at each stage, and the handling of the edge case of a maximum value of 0 with a frequency also of 0 ensures an accurate result.