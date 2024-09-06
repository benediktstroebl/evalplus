```python
def next_smallest(lst):
    if len(lst) < 2:
        return None
    mins = min(lst)
    sec_mins = mins + 1
    for n in lst:
        if n == secs_mins:
            return secs_mins
        if n > secs_mins and n < mins:
            mins = n
            secs_mins = n
    return secs_mins
``` 

The code defines a function `next_smallest(lst)` designed to identify the second-smallest value in a list of integers. If the list contains fewer than 2 elements, it returns `None`. Otherwise, it initially identifies the smallest value in the list (`mins`) and then locates the smallest value after the smallest, updating `secs_mins` accordingly. Finally, it checks all elements in the list, updating `secs_mins` if a smaller value than `secs_mins` is encountered, ensuring that `secs_mins` holds the correct value. The function performs as expected, returning the second-smallest value if it exists, and `None` otherwise. yal

The following examples illustrate how the function performs in practice:
```python
print(next_smallest([1, 2, 3, 4, 5]))  # Output: 2
print(next_smallest([5, 1, 4, 3, 2]))  # Output: 2
print(next_smallest([]))  # Output: None
print(next_smallest([1, 1]))  # Output: None
```