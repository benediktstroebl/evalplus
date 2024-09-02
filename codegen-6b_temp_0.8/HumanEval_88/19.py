
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
    new_array = list(array)
    smallest = -1
    for i in range(len(new_array)-1):
        smallest = i
        for j in range(i+1, len(new_array)):
            if new_array[i] + new_array[j] % 2 and new_array[j] > new_array[smallest]:
                smallest = j
            elif new_array[i] + new_array[j] % 2 == 0 and new_array[i] < new_array[smallest]:
                smallest = i
        if smallest != i:
            new_array[i], new_array[smallest] = new_array[smallest], new_array[i]

    return new_array

