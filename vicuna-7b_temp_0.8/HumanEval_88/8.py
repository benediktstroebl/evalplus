
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
    def count_even_or_odd_sum(array):
        # count the number of even and odd sums
        num_even = 0
        num_odd = 0
        for i in range(len(array)-1):
            if sum(array[i:i+2]) % 2 == 0:
                num_even += 1
            else:
                num_odd += 1
        return num_even, num_odd

    num_even, num_odd = count_even_or_odd_sum(array)

    if num_even % 2 != 0:
        # if the number of even sums is odd,
        # sort the array in descending order
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[j] > array[i]:
                    array[i], array[j] = array[j], array[i]

    elif num_odd % 2 != 0:
        # if the number of odd sums is odd,
        # sort the array in ascending order
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[j] > array[i]:
                    array[i], array[j] = array[j], array[i]

    else:
        # if the number of even sums is even or odd sums is even,
        # sort the array in ascending order
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[j] > array[i]:
                    array[i], array[j] = array[j], array[i]

    return array