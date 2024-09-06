Here's the improved version of the code:
```python
def how_many_times(string, sub):
    count = 0
    start = 0
    end = string.find(sub, 0, end + 1 if end != -1 else len(string))
    while start <= end:
        if string[start:end] == sub:
            count += 1
        start = end + 1
    return count
```
This updated version now uses the `find()` function to efficiently locate the substring and increment the count without overlapping. 
Additionally, the loop is updated to ensure that the start index is always less than or equal to the end index, which prevents unnecessary iterations.