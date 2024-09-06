```python
def number_of_odd(lst):
    r = []
    for i, num in enumerate(lst):
        count = sum(1 for char in num if char % 2 != 0)
        r.append(f"the number of odd elements {count}n the str{i + 1}ng {i + 1} of the {len(lst)}nput.")
    return r
```

The solution leverages Python's built-in `enumerate` feature to directly derive the string index from the iteration counter, removing the need for an additional loop to count string indices. Additionally, `sum` is employed to calculate the count of odd digits in each number, making the code more concise. The result is a more efficient and streamlined solution.