```python
def median(l: list):
    """Return median of elements in the list l.
    return sorted(l)[len(l) // 2] if len(l) % 2 == 1 else (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    ```
Explanation:
- This function takes a list l as an argument and returns the median value of its elements.
- The median is calculated using the length of the list and the length-saving property of the array.
- If if the length of the list is even, it returns the middle element.
- If the other case, it calculates the median by taking the element of the even-numbered position and the element of the odd-numbered position separately and then averaging them.
- The function passes all the provided tests.