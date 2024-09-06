Here's a Python script that contains a function called even_odd_count which takes an integer num as input and returns a tuple with the count of both odd and even digits in num. This function also has additional tests to check its correctness:
```python
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char > '9':
            continue
        elif char == '0':
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)

# Example usage:
print(even_odd_count(123))
print(even_odd_count(-12))

def even_odd_count_test():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(2000) == (3, 3)
    assert even_odd_count(67) == (1, 2)

if __name__ == "__main__":
    even_odd_count_test()
```

The script also includes a test function called even_odd_count_test, which checks the correctness of the even_odd_count function by using assert statements to verify the examples given in the problem statement. 

If the condition in the assert statement is **False**, the program will raise an AssertionError, indicating that the test has failed. This is a useful tool to test our function and ensure its correctness. 

The final line if __name__ == "__main__": ensures that the even_odd_count_test function is executed only if this script is the main entry point. This is useful for reusing the defined function in other scripts without executing the tests again.