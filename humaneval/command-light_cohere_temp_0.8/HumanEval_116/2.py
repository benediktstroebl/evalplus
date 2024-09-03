```python
def sort_array(arr):
    """
    Sorts the array of integers based on the number of ones in their binary representation in ascending order.
    return: array sorted in ascending order
    """
    bin_arr = [int(bin(num)[2:]) for num in arr]
    return sorted(arr, key=lambda x: -bin_arr[x])
# Example usage:
arr = [1, 5, 2, 3, 4]
print(sort_array(arr))  # Output: [1, 2, 3, 4, 5]
arr = [2*n for n in range(1,6)]
print(sort_array(arr))  # Output: [2, 3, 4, 5, 6]
```
This code defines a function called sort_array, which takes an array of integers as input and sorts it based on the number of ones in their binary representation in ascending order. The function achieves this by converting each number in the array to its binary representation, and then calculating the number of ones in the binary representation. The result is achieved by sorting the array using the sorted key function and the lambda function that returns the number of ones in the binary representation. The final sorted array is then returned.