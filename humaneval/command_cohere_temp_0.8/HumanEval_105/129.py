```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [ele for ele in sorted_arr if 1 <= ele <= 9]
    reversed_digits = filtered_digits[::-1]
    names = []
    for ele in reversed_digits:
        names.append(ele_to_name(ele))
    return names if names else []

def ele_to_name(ele):
    dict_map = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return dict_map[ele] if ele in dict_map else ""

# Tests
arr = [2, 1, 1, 4, 5, 8, 2, 3]
print(by_length(arr))  # Output: ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']

arr = []
print(by_length(arr))  # Output: []

arr = [1, -1 , 55]
print(by_length(arr))  # Output: ['One']
``` 

Let's break down the corrected code step by step: 
1. **Defining Variables**: We define the input array `arr` and iterate through it using a for loop, converting each digit to its corresponding name and appending it to the `names` list. 
2. **Handling Edge Cases**: We handle edge cases such as empty arrays and unexpected numbers (>9 or <1) by skipping them in the loop. 
3. **Returning Names or Empty List**: After processing all elements, the `names` list will contain the names of the digits, or an empty list if no valid digits are found. 

The function utilizes a dictionary `dict_map` to map digit integers to their respective names, allowing for more concise and readable code. 

The tests included in the script ensure that the function behaves as expected for different scenarios. 

Feel free to adapt this code snippet according to your needs! Let me know if you have any further questions.