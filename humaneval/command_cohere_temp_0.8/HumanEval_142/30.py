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

The script employs a for loop, supplemented by the `enumerate` function, to iterate through each entry in the input list `lst`. For every entry, the script evaluates the index of the entry in the list by executing `i % 3 == 0` or `i % 4 == 0 and i % 3 != 0` to decide whether the entry should be squared or cubed respectively. Subsequently, the script increments the result by the modified (or unmodified) integer entry. Finally, the function returns the value of `result`. 

Such exercises of functional programming entail understanding cases and employ a mixture of conditional statements to make decisions. While the implementation is functional, it is not the most optimal one. It would be interesting to explore a more scalable approach to this problem that leverages Python's functional programming capabilities. 

This way, we induce code reusability and maintain a clearer and smaller function by extracting the logic for squaring and cubing integers into separate functions. These can then be appended to the list of functions that are used in the main function.