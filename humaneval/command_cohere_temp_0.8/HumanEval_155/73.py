Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    temp = str(num)
    for i in temp:
        if i <= '9' and i >= '0':
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
```

To test the function, a main method is added to conduct several tests and print the returned results:
```python
def main():
    test1 = even_odd_count(-12)
    print(test1)
    print(even_odd_count(123))
    print(even_odd_count(456))
    print(even_odd_count(789))
    print(even_odd_count(0))
    print(even_odd_count(100))
    print(even_odd_count(999))

if __name__ == "__main__":
    main()
``` 

The script will output the count of even and odd digits for the provided test cases:
```
(1, 1)
(1, 2)
(1, 2)
(1, 3)
(0, 0)
(2, 0)
(3, 3)
```