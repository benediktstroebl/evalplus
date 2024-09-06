
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    # Let's do this the easy way.
    # Idea 1: for each element in the array, find the number of positions to the left it needs to get to,
    # and number of positions to the right it needs to get to.
    # Then, count the number of mismatches by adding all of those.
    # Idea 2: Greedy algorithm.
    # Start from both ends and count the number of mismatches. Then, move the pointer inward by one
    # and repeat.
    # Idea 3: use a tree. The nodes are the elements of the array, and the edges are the elements that
    # need to be flipped. We want to find the shortest path through the tree.
    # Note: for this problem, the tree is overkill. The greedy algorithm is much faster.

    # define a helper function to count number of mismatches
    # to do this, we just have to count how many elements are to the left of the current element,
    # and how many are to the right of the current element, and return their difference
    def count_mismatches(element):
        return len([item for item in arr if item < element]) - len(
            [item for item in arr if item > element]
        )

    # define a helper function to find the smallest number of mismatches
    # this is done by counting the number of mismatches with the elements to the left of the first element,
    # the elements to the right of the last element, and the element in the middle.
    def find_smallest_mismatches():
        smallest_num_mismatches = count_mismatches(arr[0])
        # for each element in the array, count the mismatches with the elements to the left and the elements to the right
        for i in range(len(arr) // 2):
            smallest_num_mismatches = min(
                count_mismatches(arr[i]),
                count_mismatches(arr[-1 - i]),
                smallest_num_mismatches,
            )
        # if the array length is even, then add the mismatches with the middle element
        if len(arr) % 2
