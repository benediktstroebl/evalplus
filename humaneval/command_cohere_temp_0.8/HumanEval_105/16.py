```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    result = []
    for num in sorted_arr:
        if str(num) in '123456789':
            result.append( arrangments[str(num)] )
    return result if result else []

arrangments = {'1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine'}
```
The code uses a dictionary Arrangments to map digits to names, and the by_length function sorts and reverses the array, filters out non-digit values, and maps digits to names. Test cases are ignored due to missing assertions.