```python
def sort_even(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
    odd.append(num)
   
    return even + odd
``` 
This function takes a list `lst` as an argument and returns a new list `result` that is the same length as `lst` but the even indices of `lst`' elements are in `even` and the odd indices are in `odd`. The function then creates two new lists `even` and `odd` and concatenates them to `result`.