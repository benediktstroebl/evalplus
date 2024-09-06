```python
def sort_third(lst):
    return sorted(lst, key=lambda x: int(x) // 3 if x % 3 == 0 else x)

# Test cases
list1 = [1, 2, 3]
assert sort_third(list1) == [1, 2, 3]

list2 = [5, 6, 3, 4, 8, 9, 2]
assert sort_third(list2) == [2, 6, 3, 4, 8, 9, 5]

list3 = [5, 6, 9, 3, 4, 2, 1]
assert sort_third(list3) == [2, 6, 3, 4, 9, 5]

list4 = [8, 6, 5, 3, 4, 2]
assert sort_third(list4) == [2, 6, 3, 4]
```
The function `sort_third` sorts a list using a key that compares each element to its integer value, then divides by three. The function handles all input values that are not divisible by three with the corresponding values that are divisible by three, and sorts them accordingly. This makes sure for any using the simple math to get a number that is divisible by three. The main logic is contained within the function and is straightforward to understand. It's a test various types of lists to determine its effectiveness.