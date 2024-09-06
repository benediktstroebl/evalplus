
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
    if len(array) < 2:
        return array
    
    def sort(array, low, high):
        # base case
        if low >= high:
            return
        
        # recursive case
        mid = (low + high) // 2
        sort(array, low, mid)
        sort(array, mid + 1, high)
        merge(array, low, mid, high)

    def merge(array, low, mid, high):
        # 1. store array into a temp array
        temp = [0 for _ in range(high - low + 1)]
        temp_index = 0

        # 2. merge
        left_index = low
        right_index = mid + 1
        while left_index <= mid and right_index <= high:
            if array[left_index] < array[right_index]:
                temp[temp_index] = array[left_index]
                left_index += 1
            else:
                temp[temp_index] = array[right_index]
                right_index += 1
            temp_index += 1
        
        while left_index <= mid:
            temp[temp_index] = array[left_index]
            left_index += 1
            temp_index += 1

        while right_index <= high:
            temp[temp_index] = array[right_index]
            right_index += 1
            temp_index += 1

        # 3. restore
        temp_index = 0
        if sum(array[low], array[high]) % 2 == 0:
            for index in range(low, high + 1):
                array[index] = temp[temp_index]
                temp_index += 1
        else:
            for index in range(high, low - 1, -1):
                array[index] = temp[temp_index]
                temp_index += 1
    
    sort(array, 0, len(array) - 1)
    return array
