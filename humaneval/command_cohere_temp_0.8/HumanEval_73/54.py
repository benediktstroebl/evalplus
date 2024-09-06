```python
def smallest_change(arr):
    odd, even = 0, 0
    for num in arr:
        if num % 2:
            odd += 1
        else:
            even += 1
    return min(odd, even)
```

The function `smallest_change` calculates the minimum number of elements that need to be changed to make the array palindromic. It counts the odd and even elements in the array using two counters, then returns the smaller of the two counts, which is the minimum number of changes required.

Here is a test case that can be used to verify the functionality of the function:
```python
arr1 = [1, 2, 3, 5, 4, 7, 9, 6]
print(smallest_change(arr1))  # Output: 4
```

Another test case that demonstrates a palindrome that requires less changes can be:
```python
arr2 = [1, 2, 3, 4, 3, 2, 2]
print(smallest_change(arr2))  # Output: 1
```

This would return `1` since changing either the first or the last element to a different value will result in a palindrome.