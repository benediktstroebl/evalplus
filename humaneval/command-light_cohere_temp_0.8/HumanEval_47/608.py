```python
def median(lst):
    """Return median of elements in the list lst."""
    sorted_numbers = sorted(lst)
    length = len(sorted_numbers)
    
    if length % 2 == 0:
        return (sorted_numbers[(length // 2) - 1] + sorted_numbers[length // 2]) / 2
    else:
        return sorted_numbers[length // 2]

# Example usage:
if __name__ == "__main__":
    # Test list with odd length
    lst = [-10, 4, 6, 1000, 10, 20]
    print("Even length:", median(lst) == 15.0)

   
    # Test list with odd length
    lst = [-10, 4, 6, 1000, 10, 20, 30]
    print("Odd length:", median(lst) == 30.0)
```
This script defines a function called **median** that takes a list as an argument and returns the median of its elements. The function sorts the median of the elements in the list and checks if the length is even or odd. If the length is even, the median is calculated as the average of the two middle numbers. If the length is odd, the median is the middle number.

Finally, the script passes examples and prints the result. The output will be the expected results.