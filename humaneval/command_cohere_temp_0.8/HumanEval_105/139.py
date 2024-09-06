```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [num for num in sorted_arr if 1 <= num <= 9]
    reversed_digits = filtered_digits[::-1]
    named_digits = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [named_digits[i] for i in reversed_digits]

# Example Usage
input_list = [2, 1, 1, 4, 5, 8, 2, 3]
print(by_length(input_list)) 

# Example Test Cases
assert by_length([]) == []
assert by_length([1, -1, 55]) == ['One']
assert by_length([4, 5, 6, 1, 2, 8]) == ['Four', 'Five', 'Six', 'One', 'Two', 'Eight']
``` 

This code first sorts the input array, then filters out only the digits 1 through 9, then reverses this filtered array, and finally uses a list composure to replace each digit with its name. The example usage and test cases demonstrate how to use the function and verify its correctness for various scenarios.