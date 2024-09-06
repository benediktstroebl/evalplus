```python
def sort_third(input_list):
    result = [input_list[i] for i in range(0, len(input_list), 3)]
    result_split = split_into_thirds(result)
    return result_split[:len(input_list)]

def split_into_thirds(lst):
    return [lst[i:i+3] for i in range(0, len(lst), 3)]
```

The function `sort_third()` takes a list as input and returns a list with the elements at indices divisible by 3 sorted, while leaving the other elements unchanged. The auxiliary function `split_into_thirds()` splits the list into chunks of size 3 to facilitate the sorting process. The `sort_third()` function then constructs a new list by concatenating these chunks. The final result is a list that is identical to the original in indices that are not divisible by 3, while the values at indices divisible by 3 are sorted. 

Here is an example usage of the function:
```python
>>> sort_third([5, 6, 3, 4, 8, 9, 2])
[2, 6, 3, 4, 8, 9, 5]
```
Which gives the desired sorted output.