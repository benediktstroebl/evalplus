```python
def search(lst):
    freq = [int(i) for i in lst if i >= 1]
    max_freq = max(freq)
    return max_freq if max_freq >= max(freq) else -1
```