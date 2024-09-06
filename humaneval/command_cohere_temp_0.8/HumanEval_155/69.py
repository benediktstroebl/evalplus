Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_odd = 0
    count_even = 0
    num_str = str(num)
    for char in num_str:
        if char > '9' or char < '0':
            if char in '-+' :
                continue
            else:
                count_odd += 1
        else:
            if int(char) % 2 == 0:
                count_even += 1
    return (count_even, count_odd)
```

This function converts the input num to a string and iterates through each digit (inclusive of '-' and '+'). It assigns odd digits to count_odd and even digits to count_even. Ultimately, it returns a tuple (count_even, count_odd).

Here is a test suite that can be used to ensure the function operates as intended:
```python
# Testing Suite
def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(15) == (2, 1)
    assert even_odd_count(1215) == (3, 2)
    assert even_odd_count(121) == (2, 1)
    assert even_odd_count(0) == (0, 0)
    assert even_odd_count(5001) == (1, 4)
    assert even_odd_count(500) == (1, 1)
    assert even_odd_count(-5001) == (1, 4)
    assert even_odd_count(-500) == (1, 1)
    assert even_odd_count("5001") == (1, 4)
    assert even_odd_count("500") == (1, 1)
```