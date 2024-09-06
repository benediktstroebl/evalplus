Here's a Python script with a self-contained function that solves the problem using Python:
```python
def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)
    
    # Check if the array itself is a palindrome
    if arr == arr[::-1]:
        return 0
    
    for i in range(len(arr)):
        # Try to find a mirror index for each element
        j = len(arr) - i - 1
        # If the element is not the same as its mirror, subtract 1 from the result
        if arr[i] != arr[j]:
            result -= 1
            # If the element and its mirror are equal, we have found a palindrome and the result is the smaller of the two
            if arr[i] == arr[j] and result > 0:
                result = 0
            # If the element and its mirror are equal multiple times, we keep subtracting 1 until we reach the palindrome
            while i + 1 < len(arr) and j + 1 < len(arr) and arr[i + 1] == arr[j + 1]:
                result -= 1
                i += 1
                j += 1
                
    return result
```

This script defines the `smallest_change` function, which calculates the minimum number of changes required to make the array palindromic. It initializes the result to the length of the array, assuming that each element will need to be changed. Then, it checks if the array is already a palindrome, In the iterative part, it examines each element of the array and its mirror index, if they are not the same, it subtracts 1 from the result. If they are the same, it checks if the result is already 0, meaning a palindrome is found. If the result is not 0, it subtracts 1 from the result as many times as possible until hitting a mirror that is not the same as its corresponding element, this ensures that the result is the minimum number of changes required.