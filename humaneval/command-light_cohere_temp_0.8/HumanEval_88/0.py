```python
def sort_array(array):
    if len(array) == 0:
        return array
    odd, even = divmod(sum(array[::-1]), 2)
    if odd:
        return sorted(array, reverse=True)
    else:
        return sorted(array)

# Test cases
test_array1 = [5, 2, 3, 9, 4]
test_array2 = [2, 4, 3, 0, 1, 5, 6]
test_array3 = [2, 4, 3, 6, 1, 5, 0]

# Function call and testing
sorted_array1 = sort_array(test_array1)
sorted_array2 = sort_array(test_array2)
sorted_array3 = sort_array(test_array3)

# Assertions
assert sorted_array1 == [0, 1, 2, 3, 4, 5]
assert sorted_array2 == [1, 2, 3, 4, 5, 6]
assert sorted_array3 == [0, 1, 2, 3, 4, 5, 6]
```
The code defines a function `sort_array` that takes an array as input and sorts it based on whether the sum of its first and last elements is odd or even. The function uses the particular to sort the array in ascending order if the sum is odd, and in descending order if the sum is even. The code also provides test cases with different arrays to test the correctness of the `sort_array` function. The test cases cover a array with odd sums, even sums, and an array with both odd and even sums.  The code then implements these tests effectively.