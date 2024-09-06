```python
def largest_smallest_integers(lst):
    positive = None
    negative = None
    for n in lst:
        if n > 0:
            if positive is None or n > positive:
                positive = n
        elif n < 0:
            if negative is None or n < negative:
                negative = n
    return (negative, positive)
```

The Python script defines a function `largest_smallest_integers` that takes a list of integers (`lst`) as input. It aims to find the largest negative integer and the smallest positive integer in the list and return them in a tuple (`(a, b)`). The function initially assigns `None` to variables `positive` and `negative`, representing the largest negative and smallest positive integers, respectively. It then iterates through the list, checking if each integer is positive or negative. If a positive integer is encountered, it compares it with the current `positive`, updating it if the new integer is larger. The same process occurs for negative integers, with the `negative` variable being updated. Finally, the function returns a tuple consisting of the largest negative integer and smallest positive integer, or `None` if neither is found in the list.