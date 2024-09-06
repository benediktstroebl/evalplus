```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    lst_sorted = []

    # Ensure that empty lists return an empty list
    if not lst:
        return lst_sorted

    for num in lst:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

        # Append the current integer, or the minimum if max_val has not been updated yet
        lst_sorted.append(min(num, max_val))
        max_val = max(max_val, num)

    return lst_sorted
```

This Python script defines a function called `strange_sort_list`. This function takes a list of integers as input and sorts it using a specified odd sorting algorithm. The sorting starts with the smallest element among the entire set of numbers, followed by the largest element among the remaining numbers, and then the smallest element among the remaining numbers, and so on. The result is then returned as a list.

The algorithm works as follows:
1. It starts by initializing the minimum and maximum values to positive and negative infinite values respectively. These variables are used to keep track of the current state of the odd sorting.
2. It initializes an empty list called `lst_sorted` where the sorted result will be stored.
3. If the input list is empty, it returns an empty list.
4. For each integer in the input list:
   - If the integer is smaller than the current minimum, it updates the minimum.
   - If the integer is larger than the current maximum, it updates the maximum.
   - It appends the smaller of the two values (the integer or the maximum) to the `lst_sorted`.
   - It updates the maximum with the larger of the two values.
5. After processing all integers, it returns the `lst_sorted` list.

Note that this function uses a "strange" sorting algorithm, which does not follow a typical sorting pattern like ascending or descending order. Instead, it mixes the ordering by selecting the next element as the minimum or maximum value remaining in the list.

Also, note that this implementation has a time complexity of O(n log n) due to the occasional updating of the maximum value. This is done twice for each element, leading to a complexity of O(n) for the append operation, and a complexity of O(log n) for finding the maximum.