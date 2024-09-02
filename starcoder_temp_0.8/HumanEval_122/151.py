
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # # The core of the problem seems to be to sort the list, and then add the
    # # sum of the smallest and largest elements. But why sort?
    # #
    # # If you look at the test case for 4 elements, you can see that the
    # # smallest and largest elements are close enough to each other to make
    # # a difference of 1 or 2. If you sort and take the sum of the first k
    # # elements, the difference is probably less than 3.
    # #
    # # I'm going to sort in place, because I can.
    # # I'm going to use a maximum heap to solve the problem.
    # # If you read about the heap data structure, you'll realize it can be
    # # used to solve the problem for k elements.
    # # The maximum heap will be used to store the first k elements of the array,
    # # and the minimum heap will be used to store the next k elements of the array.
    # #
    # # When the maximum heap is full, it will always have the greatest element.
    # # At that point, the minimum heap will be empty.
    # # If the minimum heap has at least two elements, it will always have the
    # # smallest element.
    # #
    # # The first solution I thought of was using 2 heaps.
    # # One would keep track of the largest 4 elements, the other would
    # # keep track of the smallest 4 elements.
    # # When the maximum heap was full, the smallest element would be taken out
    # # of the minimum heap and added to the maximum heap.
    # # After that, the new maximum element would be taken out of the maximum
    # # heap and added to the minimum heap.
    # #
    # # Because of the sorting, the difference in elements will always be less
    # # than 3.
    # #
    # # The time complexity is O(n log(k)), and the space complexity is O(k).
    # #
    # # For a more in-depth analysis, see this post:
    # # https://www.freecodecamp.org/news/maximum-sum-of-two-non-overlapping-elements-arrays-1/
    #
    # heap = arr[:k]
    # heapq.heapify(heap)
    #
    # for i in range(
