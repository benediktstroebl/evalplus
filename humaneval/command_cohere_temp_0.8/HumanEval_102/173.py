```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2

    if max_even >= min_even and max_even % 2 == 0:
        return max_even
    elif max_even < min_even:
        return -1
    else: 
        return choose_num(min_even, max_even)
```

The function starts by calculating the "middle" even integer between `x` and `y` - namely (`x + y`) `/ 2` and checks if this is a valid answer. If it's not valid, it gradually narrows down the search space by updating `max_even` and `min_even` based on whether the range is odd or even and satisfies the conditions of the prompt. It uses recursion to efficiently narrow down the search but avoids unnecessary recursive calls by checking the validity conditions.