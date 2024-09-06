```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2

    if max_even >= min_even and max_even % 2 == 0:
        return max_even
    elif max_even < min_even or max_even % 2 != 0:
        return -1
    else:
        return choose_num(max_even + 1, y)
```

The function uses a recursive approach to find the biggest even integer in the range, ensuring that each recursive call is bounded by validating the maximum at each level, this is inspired by The Maximum Subarray Sum Rule.

The biggest even integer is found by iteratively narrowing down the range of possibilities, first by taking the average of the maximum and minimum, and then adjusting the maximum if it's not even or if it's smaller than the minimum, the function also utilizes recursion to efficiently traverse the range.