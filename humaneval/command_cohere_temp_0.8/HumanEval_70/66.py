```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions with maximum value and even positions with minimum value.
    for i in lst:
        if i > max_val:
            max_val = i
        elif i < min_val:
            min_val = i
        elif (len(sorted_list) + 1) % 2 == 0:  # Even position, add min_val
            sorted_list.append(min_val)
            min_val = float('inf')
        else:  # Odd position, add max_val
            sorted_list.append(max_val)
            max_val = float('-inf')

    # If the remaining maximum value is smaller than minimum value, add it to the sorted list.
    if max_val < min_val:
        sorted_list.append(max_val)

    return sorted_list
```

The function odd-even transposition sorts a list in a "strange" order by alternating between the smallest and largest remaining values. This sorting method can produce varying results for different inputs. Here's how it works:
1. The function initializes `min_val` and `max_val` to positive and negative infinity, respectively. `sorted_list` is a empty list that will store the sorted values.
2. For each number in the input list, the function checks whether it is larger than the current `max_val`. If so, it updates `max_val` to the current number, since the largest value encountered thus far will be used for the next odd position.
3. If the current number is not larger than `max_val`, the function checks whether it is smaller than the current `min_val`. If so, it updates `min_val` to the current number, since the smallest value encountered thus far will be used for the next even position.
4. Regardless of the above checks, the function also checks whether the current position in the `sorted_list` is odd or even to determine whether the current `min_val` or `max_val` should be appended.
5. The final step ensures that if the remaining `max_val` is smaller than `min_val`, it means there are no more values to sort, and the remaining `max_val` is added to the end of the `sorted_list`. 

Overall, the function sorts the list in a "strange" order, where the odd positions are the largest remaining values and the even positions are the smallest remaining values, with the final value being the largest remaining value (if any).