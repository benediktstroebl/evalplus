```python
def triples_sum_to_zero(lst):
    # Initialize three empty lists
    sum_to_zero_list = [0 for _ in range(3)]
    n = len(lst)

    # Initialize a boolean list to track whether each element of the list sums to zero
    zero_sum_list = [False] * n

    # Loop through the input list
    for i, num in enumerate(lst):
        # Check if num sums to zero with the previous two numbers
        if sum_to_zero_list[0] + sum_to_zero_list[1] + num < 0:
            sum_to_zero_list[0] += num
            sum_to_zero_list[1] += num
        elif sum_to_zero_list[0] + sum_to_zero_list[1] == 0 and num != 0:
            sum_to_zero_list[2] = True
        else:
            sum_to_zero_list[2] = False

    # Check for three distinct elements that sum to zero
    return sum_to_zero_list[2]
```