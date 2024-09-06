Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")

    num_str = str(num)
    even_count = 0
    odd_count = 0

    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            even_count += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            odd_count += 1

    return (even_count, odd_count)

# Example usage
print(even_odd_count(-12))
print(even_odd_count(123))
```

This script provides the even_odd_count function with the necessary checks to ensure proper input and also provides examples to test the function. In the examples, it shows how the function handles positive and negative integers and calculates the even and odd digit counts accordingly.