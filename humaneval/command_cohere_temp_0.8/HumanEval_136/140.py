```python
def largest_smallest_integers(lst):
    negative = None
    positive = None
    for n in lst:
        if n < 0:
            if negative is None or n > negative:
                negative = n
        else:
            if positive is None or n < positive:
                positive = n
    return (negative, positive)
```

The Python script defines a function `largest_smallest_integers` that takes a list of integers as an argument. It aims to find the largest negative integer and the smallest positive integer in the list and return them in a tuple. The function initially assigns `None` to variables `negative` and `positive` for the largest negative and smallest positive, respectively. Then, it iterates through the input list, checking if each integer is negative or positive. If a negative integer is found and is larger than the previous largest found, it updates `negative`. Similarly, if a positive integer is smaller than the previous smallest found, it updates `positive`. Finally, the function returns a tuple of (largest negative, smallest positive).

Here is an example usage of the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
```

The output of this code will be:
```
(None, 1)
```

This indicates that the largest negative integer is `None` because the list does not contain any negative numbers, and the smallest positive integer is 1 as it's the first positive number in the list.