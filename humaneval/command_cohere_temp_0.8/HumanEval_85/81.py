```python
def add(lst):
    even_odd = [val for i, val in enumerate(lst) if i % 2 == 1 and val % 2 == 0]
    return sum(even_odd)
```

This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then proceeds to return the sum of these integers. The expression **enumerate(lst)**, when used in a list comprehension, can be very beneficial for understanding and debugging the filtering process, as it pairs each element with its index.

The result of the example `add([4, 2, 6, 7])` would be 2, as the function will return the sum of the even integers at odd indices, so it will sum the integer 2 from the list. 

If you have further questions or require more assistance, let me know!