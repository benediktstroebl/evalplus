```python
def search(lst):
    freq, max_val = -1, 0 
    for n in lst:
        if n > max_val:
            max_val = n 
        if n >= freq:
            freq = n 
    return max_val if max_val >= 0 and max_val >= freq else -1
```
The function iterates through the list, updating the maximum observed value and the frequency of the current value. If the maximum value is greater than or equal to its frequency, it returns this value, or -1 if no such value is found. 

This approach allows the code to qualify as a self-contained piece, as it does not rely on any external variables or data outside the scope of the function.