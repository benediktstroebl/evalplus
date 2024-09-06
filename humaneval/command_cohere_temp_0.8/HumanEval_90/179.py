```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This function sorts the input list and retrieves the second element, which should be the next smallest number. If the list has less than two elements, it returns None. Feel free to test this code with the provided test cases or your own inputs! Let me know if you have any other questions.