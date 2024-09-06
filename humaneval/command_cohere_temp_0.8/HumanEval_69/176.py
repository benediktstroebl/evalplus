```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            freq = lst.count(n)
            if freq >= n and (max_val < 0 or n > max_val):
                max_val = n
    return max_val if max_val > 0 else -1
```

The function `search` takes a list `lst` as an argument. It initially sets `freq` and `max_val` to -1 and 0, respectively. It then iterates through each integer in the list. If the integer is greater than zero, it calculates the frequency of that integer in the list (`lst.count(n)`) and determines whether the frequency is greater than or equal to the value of the integer itself. If these conditions are met and the current `max_val` is either negative or less than `n`, it updates `max_val` to `n`. 

After processing all integers in the list, the function returns `max_val` if it is greater than zero, indicating that a valid integer was found. Otherwise, it returns -1 to indicate that no such integer exists. 

This solution employs a single loop to iterate through the list, making it efficient in terms of time complexity, which is O(N), where N represents the number of elements in the input list.