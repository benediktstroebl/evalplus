
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # using Python sort() and .sort()
    return sorted(array, key=sum)

    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    # using Python list.sort()
    # array.sort(key=sum)
    # return array

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # using Python list.sort() with a lambda function
    # array.sort(key=lambda num: sum([num]))
    # return array

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # using Python sorted() with a lambda function
    # return sorted(array, key=lambda num: sum([num]))

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # using Python sorted() with a lambda function
    # return sorted(array, key=lambda num: sum([num]))

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # using Python sorted() with a lambda function
    # return sorted(array, key=lambda num: sum([num]))

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # using Python sorted() with a lambda function
    # return sorted(array, key=lambda num: sum([num]))

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # using Python sorted() with a lambda function
    # return sorted(array, key=lambda num: sum([num]))

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # using Python sorted() with a lambda function
    # return sorted(array, key=lambda num: sum([num]))

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # using Python sorted() with a lambda function
    # return sorted(array, key=lambda num: sum([num]))

    # Time
