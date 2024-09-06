Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input should be an integer")
    
    count = 0
    num_str = str(num)
    
    for char in num_str:
        if char != ' ':
            if char <= '9' and char >= '0':
                if char % 2 == 0:
                    count += 1
                else:
                    count += 0
            else:
                count += 0
    
    return count, num_str
```

To test the function, use the following code:
```python
# Testing the function
num = -12
expected_result = (1, 1)
test_result = even_odd_count(num)

assert test_result == expected_result
``` 

This will test the function with the input -12, which should return a tuple of (1, 1). 

**NOTE**: The code handles empty spaces within the number to ensure it is adaptable to different inputs. Feel free to adjust the tests accordingly.