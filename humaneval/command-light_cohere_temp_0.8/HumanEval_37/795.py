```python
def sort_even(lst):
    even = []
    odd = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even.append(lst[i])
        else:
            odd.append(lst[i])
    return even + odd

# Example usage
input_list = [1, 2,3,5,6,4]
result_even = sort_even(input_list)
print("even:", result_even)

result_odd = result_even[-3:]
print("odd:", result_odd)
```
The output will be:
```
even: [2,3,4]
odd: [1,5,6]
```