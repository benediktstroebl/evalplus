Here's a Python script that solves the given problem with an efficient algorithm using a Python list and queue:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []

    # sort even nodes
    even_nodes.sort()
    # initialize a queue for nodes indexes
    queue = []
    # Initialize index with first even node index
    min_index = even_nodes[0]
    queue.append(min_index)
    # Iterate over even nodes
    for i in range(len(even_nodes)):
        if even_nodes[i] == min_index:
            # if we have already added the smallest even node, add the next even node index
            queue.append(even_nodes[i])
        elif even_nodes[i] < min_index:
            # If we find a smaller even node, update min_index and add it to the queue
            min_index = even_nodes[i]
            queue = [min_index]
        elif even_nodes[i] > min_index:
            # if the node is greater than the current min_index, just ignore it
            pass

    return [min_index, queue.pop(0)]
```

This approach uses a combination of a list and a queue to efficiently find the smallest even value and its index. The even nodes are stored in a list and sorted in ascending order. A queue is used to keep track of node indexes. The initial index is set to the first even node value. The loop iterates over the sorted even nodes. If the current node is the same as the initial index, we append it to the queue. If it's smaller, we update the index and queue accordingly. If it's greater than the current index, we ignore it. At the end, the queue will contain the smallest even node index and its value. The output is returned as a list in the format [smallest even value, index].  The code is concise and achieves a time complexity of O(n log n) due to the sorting of the even nodes.