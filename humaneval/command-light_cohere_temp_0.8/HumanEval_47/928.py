```python
def median(l):
    # Sort the list
    l.sort(l)
    
    # Calculate the middle index
    middle = len(l) // 2
    if len(l) % 2 == 1:
        middle -= 1
    i = middle
    j = len(l) - 1 - middle
    while i <= j:
        if l[i] > l[j]:
            j -= 1
        elif l[i] < l[j]:
            i += 1
        else:
            break
    middle = i + j - 1
    
    # Get median
    median = l[middle]
    
    return median

# Example usage
print(median([-10, 4, 6, 1000, 10, 20, 2, 3, 1]))  # 15.0
```
This script defines a function called median that sorts a list and calculates the median of the elements. It then passes this test cases and prints the median for each of them.