```python
def pairs_sum_to_zero(lst):
    return any(sum(x) == 0 for x in lst)

# Test the function
test_pairsum = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [2, 4, -5, 3, 5, 7],
    [1]
]

print(pairs_sum_to_zero(test_pairsum))
```
The function pairs_sum_to_zero checks if any of the sums of the elements in the list add up to zero. If any such such would sum is zero, the function returns True; otherwise, it returns False. 

This function is self-contained, and it can be used to solve the problem and pass tests in Markdown code blocks.