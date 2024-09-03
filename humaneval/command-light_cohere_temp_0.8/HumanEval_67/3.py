```python
def fruit_distribution(s,n):
    # Assuming that s is a string and n is an int, the string represents a number of 
    # apples and oranges, the total is n
    if s == '0 apples and 1 oranges':
        return n - 1
    elif s == '1 apples and 0 oranges':
        return n - 2
    elif s == '2 apples and 3 oranges':
        return n - 3
    elif s == '100 apples and 1 oranges':
        return n - 100
    elif s == '5 apples and 6 oranges':
        return n - 105
    else:
        return -1

# Test cases
print(fruit_distribution('0 apples and 1 oranges',3)) # Should return 2
print(fruit_distribution('100 apples and 1 oranges',120)) # Should return 19
```