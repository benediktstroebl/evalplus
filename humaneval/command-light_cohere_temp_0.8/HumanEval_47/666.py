```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        raise ValueError("List must have at least two elements")
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    return median([x for x in l[::2]] + [x for x in l[-2::-2]])

#Test the function with various input
if __name__ == "__main__":
    test_input = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    test_output = median(test_input)
    print("Test 1:", test_output)
    test_input = [0, 4, 6, 8, 10, 12, 14]
    test_output = median(test_input)
    print("Test 2:", test_output)
    test_input = [-10, 4, 6, 1000, 10, 20]
    test_output = median(test_input)
    print("Test 3:", test_output)
```
This function median takes a list l as input and returns the median of the elements in that list. It does this by checking the basic preconditions: that the list must have at least two elements, and if it has an even number of elements, it simply takes the middle value. If the list has an single element (or less than two), it raises a ValueError. 

The function then loops over the list and uses the median calculation on the two middle numbers to get the median. The calculated median is then returned.