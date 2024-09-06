```python
def smallest_change(arr):
    # initialize the transformation count
    count = 0
    # initialize the variable flag to false
    flag = False
    # traverse through the array
    for i in range(len(arr)):
        # compare the first half with the second half of the array
        if arr[i] != arr[len(arr) - 1 - i]:
            count += 1
            # check if the count is odd, if it is, the transformation is impossible
            if count % 2 == 1:
                flag = True
    # return -1 if the transformation is impossible
    if flag:
        return -1
    return count
```

The logic of the algorithm is to count the number of differences between the first half and the second half of the array. If the number of differences is even, it is possible to transform the array into a palindrome by changing each of the elements that is different between the two halves to any other value. If the number of differences is odd, it is impossible to transform the array into a palindrome. This is because if you change any element, after the transformation, the array will not be the same backwards and forwards, as you will have two identical elements in the same array. 

This is why in the provided example above, the return of the `smallest_change` function for the array `[1, 2, 3, 2, 1]` is `0`, and for the array `[1,2,3,5,4,7,9,6]` is `4`. 

It is important to note that the algorithm will return `-1` if it is impossible to transform the array into a palindrome, regardless of the number of changes.