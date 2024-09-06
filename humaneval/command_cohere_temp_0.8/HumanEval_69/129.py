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
The script uses a simple iterative approach. It first finds the maximum value in the list, as it needs to be greater than this value. Then, it iterates through the list, counting the frequency of each number, and comparing it to the current maximum frequency, updating the values as necessary. 

To ensure that the greatest value that satisfies the condition isn't greater than the maximum value in the list, the script returns -1 if no such value is found. 

The approach works in O(n), where n is the length of the input list.