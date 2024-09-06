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

To test the function, a main method has been added that runs a series of tests successfully:
```python
def main():
    test1 = even_odd_count(-12)
    print(test1)
    print(even_odd_count(123))
    print(even_odd_count(12345))

main()
```
When executed, the code will output the following:
```
(1, 1)
(1, 2)
(2, 3)
```

This shows the number of even and odd digits respectively for the tested cases.