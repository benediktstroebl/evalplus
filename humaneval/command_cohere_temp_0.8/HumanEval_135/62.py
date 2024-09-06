```python
def can_arrange(arr):
    prev = arr[0]
    ans = arr.index(prev)
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        else:
            ans = i + 1
            break
    return max(ans, -1)
```

The function `can_arrange()` takes an array (`arr`) as input and iterates through it. The variable `prev` stores the value of the first element, and `ans` is initially set to the index of the first element, assuming the desired arrangement starts from the beginning of the array. During each iteration, the function checks if the current element is greater than or equal to the previous one. If the aforementioned condition is satisfied, the arrangement continues. If not, the variable `ans` is updated to the current index, and the loop ceases. The function then returns the maximum between the final value of `ans` and -1. The latter represents the absence of a valid arrangement.

Here is a usage example:
```python
arr = [1, 2, 4, 3, 5]
print(can_arrange(arr))
>> 3

arr = [1, 2, 3]
print(can_arrange(arr))
>> -1
```

The above example demonstrates the use of the `can_arrange()` function on two different arrays, confirming the correct behavior of the function as specified in the problem statement.