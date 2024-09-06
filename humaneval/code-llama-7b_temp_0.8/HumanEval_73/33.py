
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

    def first_occurrence(char):
        """
        Finds the first occurrence of char in the string
        """
        for i in range(len(arr)):
            if char == arr[i]:
                return i
        return -1

    def last_occurrence(char):
        """
        Finds the last occurrence of char in the string
        """
        for i in range(len(arr)-1, -1, -1):
            if char == arr[i]:
                return i
        return -1

    def count_occurrences(char):
        """
        Returns the number of occurrences of char in the array
        """
        count = 0
        for i in range(len(arr)):
            if char == arr[i]:
                count += 1
        return count

    # Calculate the number of occurrences of each character
    char_counts = {}
    for i in range(len(arr)):
        char = arr[i]
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Remove the single occurrences
    for char in char_counts:
        if char_counts[char] == 1:
            del char_counts[char]

    # Calculate the number of changes needed
    result = 0
    for char in char_counts:
        first = first_occurrence(char)
        last = last_occurrence(char)

        if last < first:
            first, last = last, first

        if (last - first) % 2 == 1:
            result += 1

    return result
