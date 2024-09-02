
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
    n = len(array)
    if n == 0:
        return []
    if n == 1:
        return [array[0]]

    numbers = [array[0]]
    sum_odd = 0
    sum_even = 0
    for num in array:
        if num % 2 == 0:
            sum_even += num
            numbers.append(num)
        else:
            sum_odd += num
            numbers.append(num)

    last_index = n - 1

    for i in range(1, n):
        # sum(first index value, last index value)
        total_sum = numbers[0] + sum_odd
        odd_index = [x for x in range(i, last_index + 1) if total_sum % x == 0]
        even_index = [x for x in range(i, last_index + 1) if total_sum % x == 2]

        for j in odd_index:
            numbers[j], numbers[i] = numbers[i], numbers[j]

        for j in even_index:
            numbers[j], numbers[i] = numbers[i], numbers[j]

    return numbers