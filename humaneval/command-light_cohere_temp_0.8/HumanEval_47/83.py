```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    mid = len(lst) // 2
    if lst[mid] > lst[len(lst) - 1 - mid]:
        return (median((lst[mid:])) + median((lst[:mid]))) / 2)
    else:
        return (median((lst[:mid])) + median((lst[-mid:]))) / 2)

# Example usage:
if __name__ == "__main__":
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([5, 3, 2, 4, 1]) == 2.0
    assert median([0, 5, 4, 3, 2]) == 4.0
    ```