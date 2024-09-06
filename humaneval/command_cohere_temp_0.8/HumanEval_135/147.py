```python
def can_arrange(arr):
    prev = arr[0]
    ans = arr.index(prev)
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        else:
            ans = max(ans, i)
    return max(ans, -1)
```

The function `can_arrange()` takes an array `arr` as input and iterates through it. It uses an auxiliary variable `prev` to store the value of the previous element and `ans` to store the index of the first element that is not greater than or equal to its previous element. The function continues until it finishes the entire array. If it finishes without finding an element that satisfies the conditions, the answer is -1. Otherwise, it returns the max between the found index and -1. The above approach has a time complexity of O(n) where n is the length of the array. 

Here is a markdown code block with corresponding test cases to validate the correctness of the function:
```python
def test_can_arrange():
    # Basic Cases
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    assert can_arrange([1, 2, 3]) == -1

    # Cases with consecutive elements
    assert can_arrange([1, 2, 3, 4]) == -1
    assert can_arrange([1, 4, 3, 2]) == 3

    # Cases with no valid elements
    assert can_arrange([5, 4, 3, 2]) == -1
    assert can_arrange([7, 8, 9, 10, 11]) == -1

    # Edge Case: Empty Array
    assert can_arrange([]) == -1
    ```