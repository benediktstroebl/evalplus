```python
def strange_sort_list(lst):
    # Copy list to avoid altering the original list
    result = lst[:]
    result.sort(key=lambda x: [x == min(lst), x == max(lst), x])
    return result
```

The code sorts the list `lst` in a "strange" order, where it first sorts with a key function that checks if a number is the minimum, then the maximum of the remaining numbers, and then the number itself. This creates a sort of "wave" pattern in the list where the minimum and maximum values stand out, and the rest of the list is sorted normally. The result is a list that sorts in a strange but specific order, as described in the prompt.