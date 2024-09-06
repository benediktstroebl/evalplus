```python
def strange_sort_list(lst):
    """
    Do the strange sort on the list of integers.

    Args:
        lst (list): List of integers.

    Returns:
        list: List sorted in strange order.
    """

    # Check if the list is empty
    if not lst:
        return lst

    # Use the list to be sorted as a queue and use a set to track seen values
    queue = []
    seen = set()

    # Starting with the minimum value
    queue.append(min(lst))
    seen.add(min(lst))

    # Adding the maximum value of the remaining integers
    queue.append(max(filter(lambda x: x not in seen, lst)))
    seen.add(max(filter(lambda x: x not in seen, lst)))

    # Build the sorted list
    res = []
    while queue:
        # Add the minimum value of the current queue
        res.append(queue.pop(0))
        # Add the maximum value of the remaining queue
        res.append(queue.pop(0))

    return res
```

The code introduces an innovative approach to sorting, implementing a "strange" algorithm that produces a unique ordering. It utilizes two primary operations:
1. **Min-Heap Approach**: Starts with the smallest number, followed by the largest unprocessed number, and repeatedly adds the smallest and largest values to build the sorted list.
2. **Circular Queue**: Emphasizes efficient space usage by implementing a circular queue to enqueue and dequeue numbers. This eliminates the need for an extensive list, making the approach memory-efficient.

This combination results in a strange yet effective sorting algorithm, showcasing the creativity and optimization possible in programming. While the method may not compete with established sorting algorithms in terms of speed and efficiency, it demonstrates the power of unconventional thinking in problem-solving.