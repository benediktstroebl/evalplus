def smallest_change(arr):
    # Initialize the minimum number of changes to an array length
    # Since we can change an element to any other element,
    # We can make any array palindrome with 'n' changes, where 'n' is the array length.
    min_changes = len(arr)

    # Loop through the array and reduce the min changes if a pair is found
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] != arr[j]:
                min_changes = min(min_changes, (j - i - 1) // 2)

    return min_changes