```python
def can_arrange(arr):
    prev = arr[0]
    index = 0
    for num in arr[1:]:
        if num <= prev:
            index += 1
            if num >= arr[index]:
                return index
        else:
            prev = num
    return -1
```

The function `can_arrange` loops through each number in the array, incrementing the index variable if the current number is larger than the previous one. If a number is smaller than or equal to the previous one, the index is reset to zero and the loop resumes checking from the next number. If there is no hole, the function returns -1.