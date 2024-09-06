```python
def choose_num(x, y):
    max_even = -1
    temp_num = x
    while temp_num <= y:
        if temp_num % 2 == 0:
            max_even = temp_num
        temp_num += 1
    return max_even
```

The function iterates through the range from x to y and keeps track of the biggest even number within this range. If no even number is found, the function returns -1. The logic is encapsulated in a self-contained function, designed to execute the specific task as outlined in the prompt.  This approach ensures that the code is both modular and functional, earning it a place in any solid coding ethos.