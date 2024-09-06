```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script sorts the input list and then retrieves the second smallest element, or returns None if the list has less than two elements. Feel free to adapt this solution to your needs! Let me know if you would like me to explain any part of the code further.