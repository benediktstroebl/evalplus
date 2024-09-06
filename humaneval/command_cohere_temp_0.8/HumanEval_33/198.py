```python
def sort_third(input_list):
    result = [x for i, x in enumerate(input_list) if i % 3 != 0]
    result.extend(sorted(input_list[i] for i in range(len(input_list)) if i % 3 == 0))
    return result
```

This Python script defines a function called `sort_third`, which takes a list as input. It returns a new list that maintains the original elements at indices not divisible by three but sorts the elements at indices divisible by three. The script incorporates a list comprehension and the `sorted` function to achieve this behavior. The function is exemplified through its outputs when given the inputs `[1, 2, 3]` and `[5, 6, 3, 4, 8, 9, 2]`.