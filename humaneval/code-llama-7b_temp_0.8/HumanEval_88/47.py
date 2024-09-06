
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
    def is_ascending_order(input_array):
        if len(input_array) == 0 or len(input_array) == 1:
            return True
        for index in range(1, len(input_array)):
            if input_array[index - 1] < input_array[index]:
                continue
            else:
                return False
        return True

    def merge(first_part, second_part, array):
        # 1. Set left and right pointer on the first and last index of each part of the array
        left_part_index = 0
        right_part_index = 0
        array_index = 0

        # 2. While both parts has elements left
        while left_part_index < len(first_part) and right_part_index < len(second_part):
            if first_part[left_part_index] < second_part[right_part_index]:
                array[array_index] = first_part[left_part_index]
                left_part_index += 1
            else:
                array[array_index] = second_part[right_part_index]
                right_part_index += 1
            array_index += 1

        # 3. Copy any remaining elements of first part
        while left_part_index < len(first_part):
            array[array_index] = first_part[left_part_index]
            left_part_index += 1
            array_index += 1

        # 4. Copy any remaining elements of second part
        while right_part_index < len(second_part):
            array[array_index] = second_part[right_part_index]
            right_part_index += 1
            array_index += 1

        return array

    def sort(array, start_index, end_index):
        if start_index >= end_index:
            return array
        if start_index == end_index - 1:
            if array[start_index] > array[end_index]:
                array[start_index], array[end_index] = array[end_index], array[
