
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

    def sort(array, start, end):
        if end - start < 2:
            return

        # Get middle point of given array
        middle = (start + end) // 2

        # Sort array starting from first element to middle point
        sort(array, start, middle)

        # Sort array starting from middle point to last element
        sort(array, middle, end)

        # Merge sorted arrays
        merge(array, start, middle, end)

    def merge(array, start, middle, end):
        # Merge two sorted arrays into one
        merged = []

        i = start
        j = middle

        while i < middle and j < end:
            if array[i] <= array[j]:
                merged.append(array[i])
                i += 1
            else:
                merged.append(array[j])
                j += 1

        # Append remaining array to merged array
        if i < middle:
            merged.extend(array[i:middle])
        elif j < end:
            merged.extend(array[j:end])

        # Write merged array to given array
        array[start:end] = merged

    sort(array, 0, len(array))
    return array
