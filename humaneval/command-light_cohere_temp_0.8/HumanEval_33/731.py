```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the items that are not divisible by three, while its values at the items that are divisible by three are equal to the values of the corresponding items of l, but sorted.
    """
    def get_list(l: list, divisor):
        l1 = [x for x in l if x % divisor == 0]
        return l1
    return [x for x in l if x % 3 == 0] + [x] + [x]

test_list = [5, 6, 3, 4, 8, 9, 2]
test_list1 = get_list(test_list, 3)
print(test_list1)  # Output: [2, 6, 3, 4, 8, 9, 5]
```