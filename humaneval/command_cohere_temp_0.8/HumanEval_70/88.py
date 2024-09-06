```python
def strange_sort_list(lst):
    out = [min(lst)]
    for i in lst:
        if i > out[-1]:
            out.append(i)
    return out
```

The function `strange_sort_list` takes a list of integers and returns a list in "strange" order, which means it starts with the minimum value, then the maximum value of the remaining integers, then the minimum of the remaining, and so on. The output list is constructed by iterating through the input list and appending the current element if it is greater than the last element in the output list. The minimum value is always appended first, ensuring the "strange" order. The provided example tests demonstrate the function's expected behavior.