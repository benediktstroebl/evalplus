```python
def sort_third(l: list):
    l_new = []
    for i in range(0, len(l), 3):
        try:
            temp = l[i:i+3]
            temp.sort()
            l_new.extend(temp)
        except:
            l_new.extend(l[i:i+3])
    return l_new
```
This code block implements the sort_third function, as described in the problem statement. It takes a list *l* and creates a new list *l_new*, sortying every third element in the original list. The code uses a loop to iterate over the list in increments of three, using a try-except statement to verify if each chunk is able to be sorted, incrementing a newly-created list l_new with the sorted version of the chunk, and leaving the chunk as is if it contains fewer than three elements.