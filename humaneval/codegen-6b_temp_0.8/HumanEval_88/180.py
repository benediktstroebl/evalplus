
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
    def counting_sort(array, order):
        count = [0] * (max(array) + 1)
        for element in array:
            count[element] += 1
        count = [count[i] for i in range(len(count))]
        result = [0] * len(array)
        index = 0
        for element in array:
            result[index] = count[element]
            count[element] -= 1
            index += 1
        return result

    def odd_sum(array):
        return sum(array[: len(array) // 2 + 1])

    def even_sum(array):
        return sum(array[len(array) // 2:])

    def update_array(array):
        if sum(array) % 2 != 0:
            return counting_sort(array, 1)
        else:
            return counting_sort(array, 0)

    array = list(array)
    while True:
        flag = True
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                array = update_array(array)
                flag = False
                break
        if flag:
            break
    return array

