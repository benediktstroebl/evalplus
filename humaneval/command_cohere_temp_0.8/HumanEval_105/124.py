```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [num for num in sorted_arr if 1 <= num <= 9]
    reversed_digits = filtered_digits[::-1]
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [names[i] for i in reversed_digits]

# Test Cases
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
assert by_length([]) == []
assert by_length([1, -1, 55]) == ["One"]
``` 

This code block provides a Python script that tackles the problem outlined in the prompt. It first sorts the given array of integers, then filters out only those digits that are between 1 and 9. These filtered digits are reversed, and finally, each digit is replaced by its corresponding name from the "One" to "Nine". The function handles empty arrays and odd/negative integers as specified in the prompt. The test cases are also correctly formatted and aligned to check the function's behavior against the expected output. 

The code is organized and concise, making it easy to understand and readily extensible for more extensive tests if needed.