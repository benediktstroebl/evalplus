Here's a Python script that includes a function `max_k_elements` that takes an array `arr` and an integer `k` as input, and returns a sorted list of length `k` with the maximum `k` numbers from the array:
```python
def maximum(arr, k):
    arr = sorted(arr)
    return arr[:k]

# Test Suite
def test_maximum():
    # Example 1
    input_list = [-3, -4, 5]
    k = 3
    expected = [-4, -3, 5]
    result = maximum(input_list, k)
    assert result == expected

    # Example 2
    input_list = [4, -4, 4]
    k = 2
    expected = [4, 4]
    result = maximum(input_list, k)
    assert result == expected

    # Example 3
    input_list = [-3, 2, 1, 2, -1, -2, 1]
    k = 1
    expected = [2]
    result = maximum(input_list, k)
    assert result == expected

    # Edge Case: k larger than the length of the array
    input_list = [-3, -4, 5]
    k = 4
    expected = [-3, -4, 5]
    result = maximum(input_list, k)
    assert result == expected

    # Edge Case: k = len(arr)
    input_list = [-3, -4, 5]
    k = 3
    expected = [-4, -3, 5]
    result = maximum(input_list, k)
    assert result == expected

    # Edge Case: k = 0
    input_list = [-3, -4, 5]
    k = 0
    expected = []
    result = maximum(input_list, k)
    assert result == expected

test_maximum()
```

The function sorts the input array and then returns the first `k` elements. The test suite includes examples from the prompt, as well as edge cases for handling a variety of scenarios.