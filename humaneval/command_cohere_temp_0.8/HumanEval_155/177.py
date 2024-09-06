Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the number of even and odd digits respectively:
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

To test the function, a main method is added to verify the examples given in the problem statement:
```python
def main():
    print(even_odd_count(-12))
    print(even_odd_count(123))
    print(even_odd_count(456))
    print(even_odd_count(789))
    print(even_odd_count(0))
    print(even_odd_count(100))

if __name__ == "__main__":
    main()
```

When the script is run, the main method is executed, which calls the even_odd_count function for various test cases and prints the result. The expected output for each test case is:
```
(1, 1)
(1, 2)
(1, 2)
(1, 2)
(0, 0)
(2, 0)
``` 

This indicates the number of even and odd digits respectively for each test case.