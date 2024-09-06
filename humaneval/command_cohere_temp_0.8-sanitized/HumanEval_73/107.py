def smallest_change(arr):
    # Calculate the sums of the element disparities on the first and second halves of the array
    left_sum = sum(x for i, x in enumerate(arr) if i < len(arr) // 2)
    right_sum = sum(x for i, x in enumerate(arr[::-1]) if i >= len(arr) // 2)

    # Calculate the minimum difference between the two sums
    return min(left_sum - right_sum, right_sum - left_sum)