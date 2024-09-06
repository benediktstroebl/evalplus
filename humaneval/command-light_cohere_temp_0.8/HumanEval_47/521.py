```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list must not be empty")
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test cases
for _ in range(50):
    lst = [i for i in range(100)]
    try: median(lst)
    except ValueError as e:
        print(f"Error on input list: {e}")
```
This script defines a function median that calculates the median of the elements in a list. The median is the average of the two middle values when the list is sorted in ascending order. This function handles both empty lists and lists with an odd or even number of elements.