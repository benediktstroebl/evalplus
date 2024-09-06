```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test case 1
for _ in range(50):
    a = [i for i in range(100)]
    a. = median(a)
print("Median is", a)

# Test case 2
for _ in range(50):
    a = [random.randint(1, 100) for _ in range(100)]
    a. = median(a)
print("Median is", a)
``` 
This code defines a median function that calculates the median of a list of numbers. The function first checks if the list has an even or odd number of elements, and then it uses the appropriate formula to calculate the median.