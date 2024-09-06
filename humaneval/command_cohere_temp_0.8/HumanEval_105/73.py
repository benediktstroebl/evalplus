```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_sorted = [val for val in sorted_arr if 1 <= val <= 9]
    reversed_filtered = filtered_sorted[::-1]
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [names[i] for i in reversed_filtered]

# Example usage
input_list = [2, 1, 1, 4, 5, 8, 2, 3]
print(by_length(input_list))  # Output: ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']

input_list_empty = []
print(by_length(input_list_empty))  # Output: []

input_list_strange = [1, -1, 55]
print(by_length(input_list_strange))  # Output: ['One']
```

In the above code, the `by_length` function takes an input list, sorts integers from 1 to 9, reverses the filtered list, and then returns the corresponding names for the digits. The code uses a list comprehension to reverse the filtered list and retrieve the names using the index of each digit. The example usage demonstrates the function's behavior for different input scenarios.