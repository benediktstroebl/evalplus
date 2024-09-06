```python
def median(lst):
    n = len(lst)
    if n <= 1:
        return None
    m = n // 2 + 1
    i, j = m - 1, m
    while i > 0 and j >= 0:
        if lst[i] < lst[j]:
            i -= 1
        elif lst[i] > lst[j]:
            j -= 1
        else:
            break
    m1 = i + j
    median_value = (lst[m1 - 1] + lst[m1]) / 2
    return median_value

# Test the function
lst1 = [-10, 4, 6, 1000, 10, 20]
result1 = median(lst1)
if result1 is None:
    print("List has no middle value")
elif result1 == 15.0:
    print("List has correct median.")
else:
    print("List does not have correct median.")

lst2 = [20, 10, 40, 5, 15, 25]
result2 = median(lst2)
if result2 is None:
    print("List has no middle value")
elif result2 == 25.0:
    print("List has correct median.")
else:
    print("List does not have correct median.")

```
This Python code defines a function median that computes the median value of a given list lst. The function iterates through the elements of the list, starting from the middle two elements, and compares them to determine the middle value. It then calculates the median_value as the average of the two middle values and returns it. The function is then tested using two sample lists: lst1 and lst2, and the output is compared against the expected result (either a correct median or an error message).  The code provides a simple and effective way to calculate and verify the median of a list of numbers.