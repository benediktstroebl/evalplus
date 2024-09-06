
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
    def odd_or_even(total):
        return (total & 1) == 0 or (total & 1) == 1

    def sort_helper(array, odd):
        sorted_array = []
        first = 0
        last = len(array)-1
        while first < last:
            if odd:
                if sum(array[first]) == sum(array[last]):
                    sorted_array.append(array[first])
                    sorted_array.append(array[last])
                    first += 1
                    last -= 1
                else:
                    if sum(array[first]) > sum(array[last]):
                        sorted_array.append(array[last])
                        last -= 1
                    else:
                        sorted_array.append(array[first])
                        first += 1
            else:
                if sum(array[first]) == sum(array[last]):
                    sorted_array.append(array[last])
                    sorted_array.append(array[first])
                    first += 1
                    last -= 1
                else:
                    if sum(array[first]) < sum(array[last]):
                        sorted_array.append(array[first])
                        first += 1
                    else:
                        sorted_array.append(array[last])
                        last -= 1
        return sorted_array

    # odd_or_even: bool -> (int) -> bool
    # This func will return 1 if the target odd,
    #   else return 0 if target even.
    # array: (list) -> (num) -> bool
    # This func will sort the array in ascending or descending order.
    # if the total of index value is even or odd,
    #   it would return ascending or descending order
    return sort_helper(array, odd_or_even(sum(array[0])))
