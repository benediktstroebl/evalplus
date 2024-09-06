Here's a Python script with a self-contained function that solves the problem using Python:
```python
def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)

    # Consider all possible palindromic substrings and minimize the result
    for i in range(1, len(arr)):
        for j in range(i, len(arr)):
            # Take a copy of the array since we modify it in-place
            temp_arr = arr.copy()
            # Check if the subarray [arr[i], arr[j]] is a palindrome
            if temp_arr[i-1] == temp_arr[j]:
                # If it is, remove the characters at positions i and j, and recurse
                temp_arr.pop(i)
                temp_arr.pop(j)
                result = min(result, 1 + smallest_change(temp_arr))

    return result
```

The script uses two nested loops to consider all possible palindromic substrings and determines the minimum number of changes required to make the entire array palindromic. It uses a temporary copy of the array to modify it in-place while searching for the minimum changes, and the result is updated accordingly. The function ultimately returns the minimum number of changes required to make the array palindromic.