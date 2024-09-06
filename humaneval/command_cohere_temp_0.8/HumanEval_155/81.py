Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input should be an integer")

    count_even = 0
    count_odd = 0

    num_str = str(num)
    
    # Iterate through each digit in the number
    for digit in num_str:
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
            
    return (count_even, count_odd)

# Testing the function
def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(15) == (1, 1)
    assert even_odd_count(0) == (1, 0)

test_even_odd_count()
```

Make sure to have a dedicated testing function that checks the functionality of the function for different input numbers to ensure that it follows the specified example and handles any edge cases.