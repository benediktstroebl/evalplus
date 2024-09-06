
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    # O(n) time | O(1) space
    def next_smallest(array):
        if not len(array) >= 2:
            return None
        # find the smallest number
        # smallest = min(array)
        # find the smallest number and remove it
        smallest = 2
        for num in array:
            if num < smallest:
                smallest = num
        # if smallest is None, return None
        if smallest is None:
            return None
        # remove the smallest number and find the second smallest number
        array.remove(smallest)
        second_smallest = min(array)
        return second_smallest

    # O(n) time | O(n) space
    def next_smallest_b(array):
        if not len(array) >= 2:
            return None
        smallest = array[0]
        for num in array[1:]:
            if num < smallest:
                smallest = num
        for i in range(len(array)):
            if array[i] == smallest:
                return array[i + 1]


    return next_smallest([1, 2, 3, 4, 5])

