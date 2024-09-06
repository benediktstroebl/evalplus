```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            freq = lst.count(n)
            if freq >= n:
                if n > max_val: max_val = n
    return -1 if max_val == 0 else max_val
```

The function `search` takes a list of integers `lst` as input and returns the greatest integer that is greater than zero and has a frequency greater than or equal to the value of the integer itself. To count the frequency of each integer in the list, the function initially creates a variable `freq` and sets it to negative 1, while `max_val` is initialized to 0. Then the function iterates through each integer in the list. If the current integer is greater than zero, it updates the `freq` variable to the count of how many times that number appears in the list, and checks if this frequency is greater than or equal to the number itself. If these conditions are fulfilled, the maximum value is checked again as it may have been updated during this iteration, and the function will return the integer `n` if it is greater than the current `max_val`, updating `max_val` accordingly. Finally, if no such integer is found, the function returns -1 if max_val remains 0. 

Here is an example usage of the function `search` with a list of integers:
```python
print(search([4, 1, 2, 2, 3, 1]))  # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Output: 3
print(search([5, 5, 4, 4, 4]))  # Output: -1
```