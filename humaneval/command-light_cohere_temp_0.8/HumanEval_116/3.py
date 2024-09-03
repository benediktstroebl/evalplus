```python
def sort_array(arr):
    """
    Sort an array of integers according to the number of ones in their binary representation.
    arr[:]:  If binary representation
    >>= 2
    """
    arr[:] = [int(bin(num)[2:], -1) for bin(num) in zip(''.join(arr))]
    return arr

# Test the function with various input arrays
test_array = [1, 5, 2, 3, 4]
test_array_negative = [-2, -3, -4, -5, -6]
test_array_mixed = [1, 0, 2, 3, 4]

sorted_result_test_array = sort_array(test_array)
sorted_result_test_array_negative = sort_array(test_array_negative)
sorted_result_test_array_mixed = sort_array(test_array_mixed)

print("Test Array:", json(as string)")
print(json.dumps(test_array))
print("\nSorted Array:", json(as string)")
print(json.dumps(sorted_result_test_array))

test_array_negative_result = sort_array(test_array_negative)
sorted_result_test_array_negative_result = sort_array(test_array_negative)

print("\nSorted Array with Negative Values:", json(as string))
print(json.dumps(sorted_result_test_array_negative))

test_array_mixed_result = sort_array(test_array_mixed)
sorted_result_test_array_mixed_result = sort_array(test_array_mixed)

print("\nSorted Array with Mixed Values:", json(as string))
print(json.dumps(sorted_result_test_array_mixed))
``` 
This script defines a function sort_array, which takes an array arr as input and sorts it based on the number of ones in its binary representation. It then applies this test the array with various values and verifies that the sort_array function returns the expected sorted array.