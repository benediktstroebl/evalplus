```python
def sort_even(lst):
    even = [el for el in lst if el % 2 == 0]
    return even + [el for el in lst if el % 2 != 0]

#Test cases
print("Result of sorting odd elements:")sort_even([5, 6, 3, 4])
# [3, 6, 5, 4]

print("Result of sorting even elements:")sort_even([1, 2, 3])
# [1, 2, 3]
```