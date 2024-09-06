```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list must be at least length.")
    if len(lst) == 1:
        return lst[0]
    middle = len(lst) // 2
    if lst[middle-1] > lst[middle]:
        middle1, middle2 = middle - 1, middle
    else:
        middle1, middle2 = middle, middle - 1
    return (lst[middle1] + lst[middle2]) / 2

# Test the function with sample inputs
if __name__ == "__main__":
    try:
        input_list = [-10, 4, 6, 1000, 10, 20, 30, 40, 50]
        print("Median:", median(input_list))
    except ValueError as e:
        print("Error:", str(e))
```
The provided Python code defines a function median that calculates the median value of a given list of numbers. The function handles both edge cases: when the list has no elements or is empty, it raises a ValueError, and when the list has one element, it returns that element. Additionally, it calculates the median by identifying the middle two elements, and then computes their average to obtain the median value. The code includes a test block that demonstrates the function's behavior by passing a sample list and checking if the function raises an error with the input, which is intended to validate the behavior of the median function.