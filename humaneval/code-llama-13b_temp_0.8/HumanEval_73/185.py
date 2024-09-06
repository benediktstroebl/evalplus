
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # 1. Lets get the count of each element in the array
    # 2. We need to count how many odd numbers there are (count % 2 == 1)
    # 3. If there are no odd numbers, then we need to count how many numbers have a count of 2 or more
    # 4. If there is one odd number then we need to find how many numbers have a count of 2
    # 5. If there is more than one odd number, then we need to find how many numbers have a count of 1
    # 6. Add the count of each number together
    # 7. Return the count

    # O(n) time and space
    element_counts = {}
    for element in arr:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1
    count_of_odd_numbers = 0
    count_of_elements_with_count_of_2_or_more = 0
    for element in element_counts.keys():
        if element_counts[element] % 2 == 0:
            count_of_elements_with_count_of_2_or_more += 1
        else:
            count_of_odd_numbers += 1
    if count_of_odd_numbers == 0:
        return len(arr) - count_of_elements_with_count_of_2_or_more
    if count_of_odd_numbers == 1:
        return len(arr) - count_of_elements_with_count_of_2_or_more * 2 - 1
    if count_of_odd_numbers > 1:
        return len(arr) - count_of_odd_numbers * 2













