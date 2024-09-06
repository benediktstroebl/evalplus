
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
    def sort(array, is_odd=True):
        if len(array) == 0 or len(array) == 1:
            return array
        elif len(array) == 2:
            if is_odd and sum(array) % 2 == 0:
                return array
            elif not is_odd and sum(array) % 2 == 1:
                return array
            elif sum(array) % 2 == 0:
                return [array[1], array[0]]
            else:
                return [array[0], array[1]]
        else:
            pivot = array[0]
            first_array = sort(array[1:len(array)//2+1], is_odd)
            second_array = sort(array[len(array)//2+1:], is_odd)
            return merge(first_array, pivot, second_array, is_odd)

    def merge(first_array, pivot, second_array, is_odd):
        result = []
        i, j = 0, 0
        while i < len(first_array) and j < len(second_array):
            if is_odd and sum(first_array[i]+pivot+second_array[j]) % 2 == 1:
                result.append(first_array[i])
                i += 1
            elif not is_odd and sum(first_array[i]+pivot+second_array[j]) % 2 == 0:
                result.append(first_array[i])
                i += 1
            else:
                result.append(second_array[j])
                j += 1
        if is_odd:
            if i < len(first_array):
                result.extend(first_array[i:])
                result.append(pivot)
            elif j < len(second_array):
                result.append(pivot)
                result.extend(second_array[j:])
            else:
                result.append(pivot)
            return result
        else:
            if i < len(first_array):
                result.append(pivot)
                result.extend(first_
