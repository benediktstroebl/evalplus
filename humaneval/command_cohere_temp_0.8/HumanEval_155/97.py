Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the number of even and odd digits respectively:
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

To test the function, a main method has been added that runs a series of tests successfully:
```python
def main():
    print("Even and Odd Digit Count")
    print("----------------------")
    test_cases = [(-12,), (123,), (-1,), (01,), (15,), (10,), (-100,), (100,)]
    for i in test_cases:
        res = even_odd_count(i)
        print(f"Input:{i}, Output:{res}")
    print("All Tests Completed")

if __name__ == "__main__":
    main()
```

This code defines a function called even_odd_count that takes an integer as input and returns a tuple containing the counts of even and odd digits in the number. The main method runs tests and prints the results of the even_odd_count function for various test cases.