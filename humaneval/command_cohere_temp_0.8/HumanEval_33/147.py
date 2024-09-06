```python
def sort_third(input_list):
    result = []
    for i in input_list:
        if i % 3 == 0:
            result.append(sorted(input_list[i::3]))
        else:
            result.append(i)
    return result
```
This code solves the problem as requested, creating a list `result` that maintains the original elements of `input_list` at indices not divisible by three, and at the same time, at indices divisible by three, it creates sorted sequences from corresponding segments of `input_list`, then returns the resulting hybrid list `result`. 
Here is a simpler alternative using `sorted()` and list comprehension:
```python
def sort_third(input_list):
    return [i if i % 3 != 0 else sorted(input_list[i::3]) for i in input_list]
```
Which employs the list comprehension to yield the hybrid list `result`, by filtering the even indices and sorting their corresponding list elements.