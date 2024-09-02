
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    # Use a heap to sort the integers. Since integers are comparable,
    # can use heapify. Can implement and use any other sort algorithm.

    def heapify(lst, n, i):
        '''
        Heapify the list.
        '''
        # Use i to represent the index of the current node.
        # Example: lst[i], lst[2 * i + 1], lst[2 * i + 2], ...
        # start with the left child and right child and compare them.
        # then swap if the larger one is on the left.
        # Note: lst[i] is the current node

        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        # Check if the left child of the current node is larger than
        # the current node
        if left < n and lst[left] > lst[i]:
            # If so, replace the current node with the larger
            # one and repeat the process.
            largest = left

        # Check if the right child of the current node is larger
        # than the current node
        if right < n and lst[right] > lst[largest]:
            largest = right

        # If the current node is not the largest, swap with the larger
        # one and repeat the process.
        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            heapify(lst, n, largest)

    n = len(lst)
    # Heapify the list
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)
    # Extract all the elements from the heap and return them in
    # reverse order
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    return lst
