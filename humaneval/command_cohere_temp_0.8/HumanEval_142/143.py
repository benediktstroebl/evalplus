```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The code uses a simple `for` loop to iterate through each index and entry in the provided list. It employs conditional statements to decide whether to square or cube each entry based on its index, and adds the transformed value to the `result` variable, which sums all entries. The script yields the calculated `result` as the output. 

The function correctly handles empty lists, returning 0, and also meets the conditions for the examples provided in the problem description. 

This solution is efficient and directly computes the target output with a single pass through the input list.