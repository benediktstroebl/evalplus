Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    temp = str(num)
    for i in temp:
        if int(i) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)
```

To test the function, a main method is added to execute the tests:
```python
def main():
    tests = [
        (-12, 1, 1),
        (123, 1, 2),
        (1800, 3, 5),
        (2001, 4, 6)
    ]
    for num, expected_even, expected_odd in tests:
        result = even_odd_count(num)
        assert result == (expected_even, expected_odd)

if __name__ == "__main__":
    main()
```

The function handles cases where the input num is 0, in which case it is correctly returned that both counts are 0. Then the function converts the input num into a string to iterate through each digit, counting them as either even or odd. The main method executes the function against predefined test cases, and uses the assert statement to verify the correctness of the function. 

As an automated AI language model, I encourage you to examine the code thoroughly and understand the logic and methodology behind the solution. Feel free to ask any questions or request adjustments to meet your specific requirements.