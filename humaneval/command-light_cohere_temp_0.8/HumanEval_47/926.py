```python
def median(lst):
    """Return median of elements in the list lst."""
    try:
        if len(lst) % 2 == 1:
            return (lst[int(len(lst) / 2) - 1]] + lst[int(len(lst) / 2)]) / 2
    else:
        return (lst[int(len(lst) / 2) - 1] + lst[int(len(lst) / 2)]) / 2

# Example usage
if __name__ == "__main__":
    print(median([-10, 4, 6, 1000, 10, 20] ))
    print(median([-20, -10, -15, -40]))
    print(median([1, 2, 3, 4, 5, 6]))
    print(median([10, 20, 30, 40, 50]))
```
The function median takes a list as an argument and returns the median value of its elements. This is function is self-contained, meaning that it does not use any other functions or modules, and can be easily copied and pasted anywhere. 

The function first checks if the length of the list is even or odd. If the length is even, the function calculates the median as the average of the two middle numbers of the list. If the length is odd, the function calculates the median as the average of the middle number and the last number of the list. 

The example usage demonstrates the function with various input lists, and prints the median value for each list.