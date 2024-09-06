```python
def sort_third(input_list):
    result = [input_list[i] for i in range(0, len(input_list), 3)]
    result_split = split_list(result)
    return result_split[0] + result_split[1] + result_split[2]

def split_list(lst):
    # splits list lst into three lists, assumes len(lst) is divisible by 3
    return [lst[i:i + (len(lst) // 3)] for i in range(0, len(lst), len(lst) // 3)]
```