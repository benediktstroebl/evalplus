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