
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

    if not arr:
        return 0

    even_palindrome = all(x == arr[~i] for i, x in enumerate(arr))

    if even_palindrome:
        return 0

    if len(arr) == 1:
        return 1

    if len(arr) == 2:
        return 1 if arr[0] != arr[1] else 0

    if len(arr) % 2 == 1:
        return 1

    # get the middle value
    middle = len(arr) // 2

    prefix = arr[:middle]
    suffix = arr[middle:]

    reversed_suffix = suffix[::-1]
    reversed_prefix = prefix[::-1]

    # print(prefix, suffix, reversed_suffix, reversed_prefix)

    if prefix == suffix:
        return smallest_change(reversed_prefix)

    if prefix == reversed_suffix:
        return smallest_change(reversed_suffix)

    if reversed_suffix == suffix:
        return smallest_change(prefix)

    if reversed_prefix == prefix:
        return smallest_change(suffix)

    smallest = float("inf")

    for i, x in enumerate(prefix):
        smallest = min(
            smallest,
            smallest_change(prefix[:i] + suffix)
            + smallest_change(reversed_prefix[:i] + reversed_suffix),
        )

    return smallest + 1
