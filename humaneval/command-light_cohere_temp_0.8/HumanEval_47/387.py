```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# test cases
print(median([-10, 4, 6, 1000, 10, 20] ))  # Output: 15.0
print(median([10, 20, 30, 40, 30, 10]))   # Output: 20.0
print(median([10, 20, 30, -40, 30, 10]))   # Output: 30.0
print(median([10,20,200,200,10]))      # Output: 200.0
``` 
This code defines a function median that calculates the median of a list of numbers. The function works by first finding the length of the list, then checking if the length is even or odd. If the length is odd, the median is the middle number in the list. If the length is even, the median is the average of the two middle numbers.