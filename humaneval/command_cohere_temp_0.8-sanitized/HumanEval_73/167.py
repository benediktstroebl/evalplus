def smallest_change(arr):
    # Count the number of occurrences of each element in the array
    element_counts = {}
    for num in arr:
        element_counts[num] = element_counts.get(num, 0) + 1

    # Calculate the number of changes required for each element to make the array palindromic
    change_counts = {}
    for num, count in element_counts.items():
        reverse_count = element_counts.get(arr[::-1].index(num), 0)
        change_counts[num] = abs(count - reverse_count)

    # Return the maximum number of changes from the counts
    return max(change_counts.values())