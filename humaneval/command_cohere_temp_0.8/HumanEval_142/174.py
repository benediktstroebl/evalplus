```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The script employs a for loop to iterate through each index and corresponding value in the input list `lst`. The condition `i % 3 == 0` checks if the index is a multiple of 3, triggering the squaring of the integer value. Alternatively, the condition `i % 4 == 0 && i % 3 != 0` ensures that the index is a multiple of 4 and not a multiple of 3, prompting the cubing of the integer value. Finally, the function returns the sum of all modified or original values in the list.

To ensure the effectiveness of the function, it is recommended to verify its behavior through rigorous testing cases, such as empty lists, lists with positive and negative values, and lists with both even and odd indices. 

This solution is optimized for efficiency and adheres to Python's style guidelines, making it readable and maintainable. Let me know if you'd like me to make any adjustments or additions to the code to better meet your requirements. Feel free to let me know if you would like me to explain any other Python concepts or techniques to you.