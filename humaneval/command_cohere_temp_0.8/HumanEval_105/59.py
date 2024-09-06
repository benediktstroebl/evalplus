```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [num for num in sorted_arr if 1 <= num <= 9]
    reversed_digits = filtered_digits[::-1]
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [names[idx] for idx in reversed_digits]


# Test Cases
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length([]) == []
assert by_length([1, -1, 55]) == ['One']
``` 

The function utilizes several steps to solve the problem statement:
1. **Sorting Numbers**: The provided array is sorted, arranging the numbers in sequential order. 
2. **Filtering Digits**: The sorted array is filtered to retain only those numbers between `1` and `9`. 
3. **Reversing Digits**: The filtered digit array is reversed, ensuring the digits are in reverse order. 
4. **Replacing Digits with Names**: The reversed digit array is mapped to their respective names from the predefined list, resulting in the names being arranged in the reverse order of their corresponding digits. 

The test cases are designed to validate the behavior of the function against the expected output for various scenarios.  If the function's output matches the expected for all test cases, the function is correctly implemented and working as intended. 

You can use these tests to validate your code and ensure it complies with the problem statement. Test your function using these tests to ensure it conforms with the problem statement. Feel free to modify the tests to include more scenarios or refine existing ones to match your needs. In a self-contained manner, the offered code provides a resolution to the problem statement and enables independent usage and examination of the function.  If you have any questions or need assistance, please let me know! I'll be delighted to help!